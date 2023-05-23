from flask import Flask,render_template,request,url_for,redirect,session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/",methods=(["GET","POST"]))
def home():
    if not session.get("user"):
        return redirect("/login")
    if request.method == 'POST':
        session["user"] = None
        return redirect("/")
    user = session["user"]
    return render_template("index.html",user = user)
    

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get("user")
        session["user"] = user
        return redirect("/")
    
@app.route("/notes",methods=(['GET','POST']))
def notes():
    user = session["user"]
    return render_template("notes.html",user=user)

if __name__=='__main__':
    app.run(debug=True)