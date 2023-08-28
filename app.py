# app.py

from flask import Flask, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.debug = True
app.config.from_object('config.Config')

# Create the SQLAlchemy instance AFTER configuring the app.
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define your User model here (model.py).

class User(db.Model):
    __tablename__ = 'user'

    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(300), nullable=False)

@app.route('/register', methods=['GET', 'POST'])
def Register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not User.query.filter_by(username=username).first():
            hashed_password = generate_password_hash(password, method='scrypt')
            new_user = User(username=username, password=hashed_password)
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

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            flash('Login successful.', 'success')
            # Redirect to the profile page (index.html)
            return redirect(url_for('profile'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/index')
def profile():
    return render_template('index.html')

@app.route('/agent')
def agent():
    return render_template('agent.html')

if __name__ == '__main__':
    app.run()
