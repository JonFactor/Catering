# store routes
### imports
from flask import Blueprint, render_template # organize files
from flask_login import current_user, login_required, login_user, logout_user
### code
views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('Home.html', user = current_user)