from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())  #storing date autometically
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  #when one user has many notes, the forienkey attaches the note to a specific id 


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Weight = db.Column(db.String(3))
    RPE = db.Column(db.String(1)) 
    set_num = db.Column(db.String(1)) 
    date = db.Column(db.DateTime(timezone=True), default=func.now()) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #this lets notes be insynched with id 
    workout = db.relationship('Workout')

