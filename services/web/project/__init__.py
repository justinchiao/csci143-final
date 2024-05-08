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
import sqlalchemy
import datetime

app = Flask(__name__)

engine=sqlalchemy.create_engine("postgresql://postgres:pass@postgres:5432", connect_args={'application_name':'__init__.py'})
connection=engine.connect()

def are_creds_good(user,pw):
    #look into db and find
    sql = sqlalchemy.sql.text("""
        SELECT id FROM users
        WHERE username = :user
        and password = :pw;
            """)
    res = connection.execute(sql, {
        'user':user,
        'pw':pw
    })

    if res.first() is None:
        return False
    else:
        return True

def root_chirps(page):
    sql = sqlalchemy.sql.text("""
        SELECT * from chirps
        ORDER BY created_at DESC
        LIMIT 20 OFFSET :offset;
            """)
        
    res = connection.execute(sql, {'offset':(page)*20})
    chirps=[]
    for chirp in res.fetchall():
        id_user=chirp[1]
        time=chirp[2]
        text=chirp[3]
        sql = sqlalchemy.sql.text("""
            SELECT user_name from users
            WHERE id_users=:id;
                """)
        username = connection.execute(sql, {'id':id_user}).fetchone()[0]
        chirps.append({
            'username':username,
            'text':text,
            'time':time
        })
    return chirps

@app.route("/")
def hello_world():
    #check if logged in
    username=request.cookies.get('username')
    password=request.cookies.get('password')
    if request.cookies.get('loggedIn')=='true':
        good_credentials=True
    else:
        good_credentials=False
    page=int(request.args.get('page',0))
    chirps=root_chirps(page)

    return render_template('root.html', logged_in=good_credentials, chirps=chirps, page=page) 

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

            template = render_template('root.html', bad_credentials=False, logged_in=True)
            response = make_response(template)
            response.set_cookie('username', username)
            response.set_cookie('password', password)
            response.set_cookie('loggedIn', 'true')
            return response

    return render_template('login.html')

@app.route("/logout", methods=["GET", "POST"])
def logout():
    response = redirect('/')
    #response.CookieJar.clear()
    response.set_cookie('username', max_age=0)
    response.set_cookie('password', max_age=0)
    response.set_cookie('loggedIn', max_age=0)
    return response

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.cookies.get('loggedIn')=='true':
        good_credentials=True
        return render_template('root.html', logged_in=good_credentials)
    else:
        good_credentials=False
    username=request.form.get("username")
    #find if this username already exists in user
    
    firstName=request.form.get("firstname")
    lastName=request.form.get("lastname")
    #find current largest user_id, increment 


@app.route("/create_chirp", methods=["GET", "POST"])
def create_chirp():
    if request.cookies.get('loggedIn')=='true':
        good_credentials=True
    else:
        good_credentials=False
    chirp=request.form.get("chirp")
    #get user id info
    #add to database
    return render_template('create_chirp.html', logged_in=good_credentials)

@app.route("/search", methods=["GET", "POST"])
def search():
    pass
