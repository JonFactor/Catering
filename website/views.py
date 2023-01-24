# imports
from flask import Blueprint, render_template

# define this file is a blueprint
views = Blueprint('views', __name__)

# url
@views.route('/')

# function will run when url called
def home():
    return render_template("home.html") # html code

