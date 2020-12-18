from flask import Flask, render_template, redirect
from flask.helpers import url_for
from wtform import *
from models import *
from datetime import datetime, timedelta
from passlib.hash import pbkdf2_sha256


app = Flask(__name__)
app.secret_key="later"

app.config['SQLALCHEMY_DATABASE_URI']="postgres://zlcsxccctwmvdp:b2b27bc4b07b3b309412b7c51e0483eaea106ba964509517379406b3ae762bf4@ec2-34-194-198-238.compute-1.amazonaws.com:5432/d35q9ogcrt02v1"
db = SQLAlchemy(app)

@app.route("/",methods=["GET", "POST"])
def index():

    reg_form = RegForm()
    
    #registration is successful and route the user into login page
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        name = reg_form.name.data
        surname = reg_form.surname.data
        email = reg_form.email.data
        password = reg_form.password.data

        hashed_pw = pbkdf2_sha256.hash(password)

        createdate = datetime.now()
 

        user = User(username=username, password=hashed_pw, name=name, surname=surname,email=email,createdate=createdate)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("index.html",form=reg_form)


@app.route("/login",methods=["GET", "POST"])
def login():

    login_form = LogForm()

    if login_form.validate_on_submit():
        return "Log into the system."
    
    return render_template("login.html", form=login_form)


if __name__=="__main__":
    app.run(debug=True)

