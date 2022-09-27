from .db import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer , Enum
import enum

class UserTypes(enum.Enum):

    administrator = 1
    regular_user = 2
    
class OperationTypes(enum.Enum):
    
    create = 1
    take = 2
    add = 3
    change = 4   
    
    
class Item(db.Model):
    
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(50) ,nullable = False)
    cellId = db.Column(db.Integer , primary_key = False)
    count = db.Column(db.Integer, default = 0)
    description = db.Column(db.String(200) ,nullable = True)

class User(db.Model):
    
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(50) ,nullable = False)
    email = db.Column(db.String(50) ,nullable = False)
    password = db.Column(db.String(50) ,nullable = False)
    type = db.Column(Enum(UserTypes), nullable = False)

class Operation(db.Model):
    
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer, nullable = False )
    item_id = db.Column(db.Integer, nullable = False )
    amount = db.Column(db.Integer, nullable = False )
    type = db.Column(Enum(OperationTypes) , nullable = False)
