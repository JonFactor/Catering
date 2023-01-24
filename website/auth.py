# imports
from flask import Blueprint

# define this file is a blueprint
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '1'

@auth.route('/Logout')
def Logout():
    return '2'

@auth.route('/SignUp')
def SignUp():
    return '3'