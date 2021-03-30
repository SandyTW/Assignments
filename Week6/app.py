from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import g


app=Flask(__name__)
app.secret_key = '\x00\xa1\x85\nv\xd9;D'

@app.route("/")
def home():
    return render_template("WK6Index.html")

@app.route("/signin", methods=["POST"])
def verified():
    name=request.form["nameColumn"]
    password=request.form["passwordColumn"]
    if name =='test' and password =='test':
        session['user'] = name
        return redirect("/member/")
    else:
        return redirect("/error/")

@app.route("/member/")
def verifiedMember():
    if g.user:
        return render_template("IndexMember.html", user=session['user'])
    return redirect("/")

@app.route("/error/")
def verifiedError():
    return render_template("IndexError.html")

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
    