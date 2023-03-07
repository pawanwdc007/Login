import mysql.connector
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def login():
    return render_template('main_login.html')

@app.route('/auth', methods=['POST'])
def auth():
    # Get form data
    username = request.form['username']
    password = request.form['password']

    db = mysql.connector.connect(
        host="localhost",
        user="pawan",
        password="*********",
        database="mtech"
    )
    sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
    val = ("john", "password123")
    mycursor.execute(sql, val)

    mydb.commit()

    # Check if username and password are correct
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        # User is authenticated
        session['username'] = user[1]
        return redirect('/welcome')
    else:
        # User is not authenticated
        return redirect('/')

def dashboard():
    # Check if user is authenticated
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect('/')
