from app import db

class User(db.Model):
    __tablename__ = 'user'

    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(300), nullable=False)

class Clients(db.Model):
    __tablename__='clients'
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False,primary_key=True)
    message = db.Column(db.Text)

class Agent(db.Model):
    
    __tablename__='agent'
    
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False,primary_key=True)
    comment = db.Column(db.Text)   
class Contact(db.Model):
    __tablename__='contact'
    
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False,primary_key=True)
    
    comment = db.Column(db.Text)      
