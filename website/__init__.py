# imports
from flask import Flask

def createApp():
    # make this file the flask server file
    app = Flask(__name__) 

    # encryption key
    app.config['SECRECT_KEY'] = 'joeroganisprettyshorttbh'

    # import blueprints
    from .views import views
    from .auth import auth

    # use blueprints
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app