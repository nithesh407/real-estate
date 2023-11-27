from flask import Flask,make_response, redirect, render_template, request, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail,Message
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__, static_url_path='/static')
app.debug = True
app.config.from_object('config.Config')
app.config['DEBUG'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail_app = Mail(app)

import models


def auth():
    cookie = request.cookies.get('loggedin')
    return cookie != 'True'

@app.route('/register', methods=['GET', 'POST'])
def Register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not models.User.query.filter_by(username=username).first():
            hashed_password = generate_password_hash(password, method='scrypt')
            new_user = models.User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = models.User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            flash('Login successful.', 'success')

            session['user_id'] = user.username

            # Convert boolean to string before setting the cookie
            # Convert boolean to string before setting the cookie
            logged_in_str = str(True)

            # Use make_response to set the cookie and perform the redirect
            resp = make_response(redirect(url_for('profile')))
            resp.set_cookie('loggedin', logged_in_str)

            return resp
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/index')
def profile():
    
    if(auth()):
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

@app.route('/prithivi',methods=['GET','POST'])
def prithivi():
    if(auth()):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            message = request.form['message']

            # You can perform any validation or additional checks here
            send_email(firstname,email,message,'prithivirajp.21cse@kongu.edu')
            new_user = models.Clients(
                firstname=firstname,
                lastname=lastname,
                email=email,
                message=message
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. Please log in.', 'success')
        return render_template('prithivi.html')

@app.route('/pranesh',methods=['GET','POST'])
def pranesh():
    if(auth()):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            message = request.form['message']

            # You can perform any validation or additional checks here
            send_email(firstname,email,message,'praneshac.21cse@kongu.edu')
            new_user = models.Clients(
                firstname=firstname,
                lastname=lastname,
                email=email,
                message=message
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. Please log in.', 'success')
        return render_template('pranesh.html')

@app.route('/Nithesh',methods=['GET','POST'])
def nithesh():
    if(auth()):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            message = request.form['message']

            # You can perform any validation or additional checks here

            new_user = models.Clients(
                firstname=firstname,
                lastname=lastname,
                email=email,
                message=message
            )
            db.session.add(new_user)
            db.session.commit()
            mailto = 'nitheshr.21cse@kongu.edu'
            send_email(firstname, email, message , mailto)
            flash('Registration successful. Please log in.', 'success')
        return render_template('nithesh.html')

@app.route('/nix',methods=['GET','POST'])
def nix():
    if(auth()):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            message = request.form['message']

            # You can perform any validation or additional checks here
            send_email(firstname,email,message,'niganths.21cse@kongu.edu')
            new_user = models.Clients(
                firstname=firstname,
                lastname=lastname,
                email=email,
                message=message
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. Please log in.', 'success')
        return render_template('nix.html')

@app.route('/agents')
def agents():
    if(auth()):
        return redirect(url_for('login'))
    else:
        return render_template('agents.html')

@app.route('/property')
def property():
    if(auth()):
        return redirect(url_for('login'))
    else:
        return render_template('property-grid.html')

@app.route('/propertysingle',methods=['GET','POST'])
def propertysingle():
    if(auth()):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            
            name = request.form['name']
            email = request.form['email']
            comment = request.form['comment']

            # You can perform any validation or additional checks here

            new_user = models.Agent(
                
                name=name,
                email=email,
                comment=comment
            )
            db.session.add(new_user)
            db.session.commit()
            
        return render_template('property-single.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    if(auth()):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            
            name = request.form['name']
            email = request.form['email']
        
            comment = request.form['comment']

            # You can perform any validation or additional checks here

            new_user = models.Contact(
                
                name=name,
                email=email,
            
                comment=comment
            )
            db.session.add(new_user)
            db.session.commit()
            mailto = 'americanbrokers01@gmail.com'
            send_email(name, email, comment,mailto)
            
        return render_template('contact.html')
    
def send_email(name, email, comment,recipient):
    subject = 'New Contact Form Submission'
    body = f'Name: {name}\nEmail: {email}\nComment: {comment}'

    message = Message(subject,sender=email, recipients=[recipient], body=body)

    try:
        mail_app.send(message)
        print('Email sent successfully.')
    except Exception as e:
        print(f'Error sending email: {e}')    


if __name__ == '__main__':
    app.run()
