from flask import Flask, jsonify, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

import psycopg2 
import psycopg2.extras

app = Flask(__name__)

load_dotenv()

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


#Connect to database
def get_db_connection():
    # Get all db environments from .env 
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
    return conn

@app.route('/')
def home():
    if 'email' in session:
        email = session['email']
        return jsonify({'message' : 'You are already logged in', 'email' : email})
    else:
        resp = jsonify({'message' : 'Unauthorized'})
        resp.status_code = 401
        return resp
#Sign up 
@app.route('/signup', methods=['POST'])
def signup():
    _json = request.json
    _email = _json['email']
    _password = _json['password']
    # Validate the received values request
    if _email and _password:
        #Check user exists
        conn = get_db_connection()
        # Setting auto commit to True
        conn.autocommit = True

        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
        sql = "SELECT * FROM accounts WHERE email=%s"
        sql_where = (_email,)
          
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        if row != None:
            resp = jsonify({'message' : 'This email has already signed up!'})
            resp.status_code = 400
            return resp
        else:
            #Hash password before saving into database
            _password = generate_password_hash(_password)
            sql = "INSERT INTO accounts (EMAIL, PASSWORD) VALUES (%s, %s)"
            record_insert = (_email, _password)
            cursor.execute(sql, record_insert)

            return jsonify({
                'message': 'Signup successfully!'
            })

@app.route('/login', methods=['POST'])
def login():
    _json = request.json
    _email = _json['email']
    _password = _json['password']
    # validate the received values
    if _email and _password:
        #check user exists
        conn = get_db_connection()          
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
          
        sql = "SELECT * FROM accounts WHERE email=%s"
        sql_where = (_email,)
          
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()

        if row == None:
            resp = jsonify({
                'message': 'Cannot find this user, please sign up!'
            })
            resp.status_code = 400
            return resp
        else:
            isMatch = check_password_hash(row['password'], _password)
            if not isMatch:
                resp = jsonify({
                    'message': 'Invalid password!'
                })
                resp.status_code = 400
                return resp
            else:
                #Create a session 
                session['email'] = row['email']
                return jsonify({
                    'message': 'Login successfully!'
                })
          
@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
    return jsonify({'message' : 'You successfully logged out'})
          
if __name__ == "__main__":
    app.run(use_reloader=True)
