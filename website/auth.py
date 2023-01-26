# imports
from flask import Blueprint, render_template

# define this file is a blueprint
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html',boolean = True)

@auth.route('/logout')
def logout():
    return '<t>Logging OUT</t>'

@auth.route('/SignUp')
def signup():
    return render_template('signup.html')