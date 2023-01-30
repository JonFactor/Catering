### imports
from flask import Blueprint, render_template, request, flash, redirect, url_for # organize files
from .models import User, db, Order
from werkzeug.security import generate_password_hash, check_password_hash # hashes dont have inverses
from flask_login import login_user, logout_user, login_required, current_user
### code
auth = Blueprint('auth', __name__)

@auth.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        email = form.get('email')
        password = form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Sign In Successful', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Invalid password', category='error')
        else:
            flash('Invalid email', category='error')
    return render_template('signin.html', user = current_user)


@auth.route('/signout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        form = request.form

        email = form.get('email')
        name = form.get('name')
        password1 = form.get('password1')
        password2 = form.get('password2')
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be at least 4 characters long', category='error')
        elif len(name) < 2:
            flash('Name must be at least 2 characters long', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters long', category='error')
        elif password1 != password2:
            flash('Passwords do not match')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Sign up successful', category='success')
            redirect(url_for('auth.signin'))
    return render_template('signup.html', user = current_user)

@auth.route('/order', methods=['GET', 'POST'])
@login_required
def orders():
    if request.method == 'POST':
        form = request.form
        ordernum = 0
        if int(form.get('meat')):
            ordernum +=  int(form.get('meat')) 
        if int(form.get('sides')):
            ordernum +=  int(form.get('sides')) 
        if int(form.get('drinks')):
            ordernum +=  int(form.get('drinks')) 
        if int(form.get('people')):
            ordernum +=  int(form.get('people')) 

        new_order = Order(ordernum = ordernum)
        db.session.add(new_order)
        db.session.commit()
    else:
        pass
    return render_template('order.html', user = current_user)

@auth.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        deleteid = request.form.get('del')
        db.session.delete(Order.query.filter_by(id=deleteid).first())
    return render_template('adminportal.html', query=Order.query.all(), user=current_user)