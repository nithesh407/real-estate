from flask import Flask, redirect, render_template, request, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.debug = True
app.config.from_object('config.Config')
app.config['DEBUG'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models

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
