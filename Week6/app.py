from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=" ",
  database="website"
)
mycursor = mydb.cursor()
cnx=mydb.cursor(dictionary=True)

app=Flask(__name__)
app.secret_key = '\x00\xa1\x85\nv\xd9;D'


@app.route("/")
def home():
    return render_template("WK6Index.html")


@app.route("/signup", methods=["POST"])
def Register():
    username=request.form["usernameRegister"]
    name=request.form["nameRegister"]
    password=request.form["passwordRegister"]
    cnx.execute('SELECT * FROM user WHERE username = %s', (username,))
    CurrentUser=cnx.fetchone()
    if CurrentUser:
        return redirect("/error/?message=帳號已經被註冊")
    else:
        cnx.execute('INSERT INTO user VALUES (default, %s, %s, %s, default)', (name, username, password))
        mydb.commit()
        return redirect('/')


@app.route("/signin", methods=["POST"])
def verified():
    username=request.form["nameColumn"]
    password=request.form["passwordColumn"]

    cnx.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password))
    CurrentUser=cnx.fetchone()
    if CurrentUser: 
        session['name']=CurrentUser['name']
        session['username']=CurrentUser['username']
        return redirect('/member/')
    else:
        return redirect('/error/?message=帳號或密碼輸入錯誤')
        

@app.route("/member/")
def verifiedMember():
    if 'username' in session:
        return render_template("IndexMember.html")
    else:
        return redirect("/")


@app.route("/error/")
def verifiedError():
    data=request.args.get("message", None)
    return render_template("IndexError.html", msg=data)


@app.route('/signout')
def dropsession():
    session.pop('name', None)
    session.pop('username', None)
    return redirect("/")


if __name__=="__main__":
    app.run(port=3000)
    
