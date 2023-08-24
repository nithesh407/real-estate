from flask import Flask, render_template, request, send_file



app = Flask(__name__)


@app.route('/')
def login():
   

    return render_template("login.html")
@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/index')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
