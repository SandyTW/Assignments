from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import g

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Tj920419#!",
  database="website"
)
mycursor = mydb.cursor()
cnx=mydb.cursor(dictionary=True)

app=Flask(__name__)
app.secret_key = '\x00\xa1\x85\nv\xd9;D'

@app.route("/")
def home():
    return render_template("WK6Index.html")


# @app.route("/signup", methods=["POST"])
# def Register():







@app.route("/signin", methods=["POST"])
def verified():
    username=request.form["nameColumn"]
    password=request.form["passwordColumn"]

    cnx.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password))
    account = cnx.fetchone()
    if account: 
        session['user']=account['username']
        return redirect('/member/')
    else:
        return redirect("/error/")

    # if name =='test' and password =='test':
    #     session['user'] = name
    #     return redirect("/member/")
    # else:
    #     return redirect("/error/")

@app.route("/member/")
def verifiedMember():
    if g.user:
        return render_template("IndexMember.html", user=session['user'])
    return redirect("/")

@app.route("/error/")
def verifiedError():
    msg='帳號或密碼輸入錯誤'
    return render_template("IndexError.html", data=str(msg))


@app.before_request
def beforeRequest():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/signout')
def dropsession():
    session.pop('user', None)
    return redirect("/")


if __name__=="__main__":
    app.run(port=3000)
    