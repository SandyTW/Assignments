from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

app=Flask(__name__)
# , static_folder="public", static_url_path="/"

@app.route("/")
def home():
    return render_template("WK4Index.html")

@app.route("/member/")
def verifiedMember():
    return render_template("IndexMember.html")

@app.route("/error/")
def verifiedError():
    return render_template("IndexError.html")

@app.route("/signin", methods=["POST"])
def verified():
    name=request.form["nameColumn"]
    password=request.form["passwordColumn"]
    if name=='test' and password=='test':
        return redirect("/member/")
    else:
        return redirect("/error/")


if __name__=="__main__":
    app.run(port=3000)
    