### imports
# . = current package
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# making and setting colums for tables
class Order(db.Model, UserMixin): # child
    __tablename__ = "Order"
    id = db.Column(db.Integer, primary_key=True)
    ordernum = db.Column(db.Integer, index=True, unique=False)
    date = db.Column(db.DateTime(timezone= True), default= func.now())
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)

class User(UserMixin, db.Model): # parent
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(68), index=True, unique=False)
    name = db.Column(db.String(70), index=True, unique=False)
    orders = db.relationship('Order', backref='user')