import os
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    render_template,
    make_response,
    redirect
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


#app = Flask(__name__)
#app.config.from_object("project.config.Config")
#db = SQLAlchemy(app)

engine=sqlalchemy.create_engine("postgresql://

def are_creds_good(user,pw):
    #look into db and find 
    if user=='justin' and pw=='1234':
        return True
    else:
        return False

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route("/")
def hello_world():
    #check if logged in
    username=request.cookies.get('username')
    password=request.cookies.get('password')
    good_credentials=are_creds_good(username,password)

    messages=['query', 'query']
    return render_template('root.html', logged_in=good_credentials, messages=messages) 

@app.route("/login", methods=["GET", "POST"])
def login():
    username=request.form.get("username")
    password=request.form.get("password")
    
    good_credentials = are_creds_good(username,password)

    if username is None:
        return render_template('login.html', bad_credentials=False)
    else:
        if not good_credentials:
            return render_template('login.html', bad_credentials=True)
        else:

            template = render_template('login.html', bad_credentials=False, logged_in=True)
            response = make_response(template)
            response.set_cookie('username', username)
            response.set_cookie('password', password)
            return response

    return render_template('login.html')

@app.route("/logout", methods=["GET", "POST"])
def logout():
    response = redirect('/')
    response.set_cookie('username','password', max_age=0)
    return response

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    pass
@app.route("/create_chirp", methods=["GET", "POST"])
def create_message():
    pass
@app.route("/search", methods=["GET", "POST"])
def search():
    pass
