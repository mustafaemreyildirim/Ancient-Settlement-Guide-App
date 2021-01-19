from re import search
from flask import Flask, render_template, redirect
from flask.globals import current_app
from flask.helpers import url_for
from wtform import *
from models import *
from datetime import datetime
from flask_login import LoginManager, login_user,current_user, login_required, logout_user
from remade_model import *


app = Flask(__name__)
app.secret_key="later"

app.config['SQLALCHEMY_DATABASE_URI']="postgres://zlcsxccctwmvdp:b2b27bc4b07b3b309412b7c51e0483eaea106ba964509517379406b3ae762bf4@ec2-34-194-198-238.compute-1.amazonaws.com:5432/d35q9ogcrt02v1"
db = SQLAlchemy(app)

login = LoginManager(app)
login.init_app(app)


@login.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route("/",methods=["GET", "POST"])
def home():
    return render_template("enterance.html")

@app.route("/register",methods=["GET", "POST"])
def register():

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
 

        user = User_remade(username,hashed_pw,email,createdate,name,surname)
        user.insert()

        #user = User(username=username, password=hashed_pw, name=name, surname=surname,email=email,createdate=createdate,prfimg=prfimg)
        #db.session.add(user)
        #db.session.commit()
        return redirect(url_for('login'))

    return render_template("index.html",form=reg_form)


@app.route("/login",methods=["GET", "POST"])
def login():

    login_form = LogForm()

    if login_form.validate_on_submit():
        user=User.query.filter_by(username=login_form.username.data).first()
        login_user(user)
        if current_user.is_authenticated:
            return redirect(url_for('cities'))
    
    return render_template("login.html", form=login_form)


@app.route("/cont_register",methods=["GET", "POST"])
def index():

    reg_form = ContRegForm()
    
    #registration is successful and route the user into login page
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        name = reg_form.name.data
        surname = reg_form.surname.data
        email = reg_form.email.data
        university = reg_form.university.data
        researcharea = reg_form.researcharea.data
        password = reg_form.password.data

        hashed_pw = pbkdf2_sha256.hash(password)

        createdate = datetime.now()
        prfimg = reg_form.prfimg
 

        cont = Contributor(username=username, password=hashed_pw, name=name, surname=surname,email=email,createdate=createdate,university=university,researcharea=researcharea,prfimg=prfimg)
        user = User(username=username, password=hashed_pw, name=name, surname=surname,email=email,createdate=createdate,prfimg=prfimg)
        db.session.add(cont)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('cont_login'))

    return render_template("reg_index.html",form=reg_form)


@app.route("/cont_login",methods=["GET", "POST"])
def cont_login():

    login_form = LogForm()

    if login_form.validate_on_submit():
        cont=User.query.filter_by(username=login_form.username.data).first()
        login_user(cont)
        if current_user.is_authenticated:
            return redirect(url_for('cities'))
    
    return render_template("reg_login.html", form=login_form)


@app.route("/profile/<username>",methods=["GET", "POST"])
def profile(username):
    user = User.query.filter_by(username=username).first()
    cont = Contributor.query.filter_by(username=username).first()
    
    message=0
    if cont:
        message = 1
        return render_template("cont_profile.html",user=user,cont=cont,message = message)
    return render_template("profile.html",user=user,message=message)

@app.route("/add_cities", methods=["GET", "POST"])
def add_cities():
    
    set_form = AnSetForm()
    
    if set_form.validate_on_submit():
        cityname = set_form.cityname.data
        location = set_form.location.data
        region = set_form.region.data
        civilization = set_form.civilization.data
        knownperson = set_form.knownperson.data
        description = set_form.description.data
        img = set_form.img.data

        if Region.query.filter_by(region=region).first()==None:
            reg_add = Region(region=region)
            db.session.add(reg_add)
            db.session.commit()
        if Knownperson.query.filter_by(knownperson=knownperson).first()==None: 
            kn_add = Knownperson(knownperson=knownperson)
            db.session.add(kn_add)
            db.session.commit()
            
        return redirect(url_for('cities'))

    return render_template("add_ancient_settlement.html",form=set_form)

@app.route("/add_paths", methods=["GET", "POST"])
def add_paths():
    return render_template("add_paths.html")


@app.route("/cities",methods=["GET", "POST"])
def cities():

    username = current_user.get_username()
    user = User.query.filter_by(username=username).first()
    cont= Contributor.query.filter_by(username=username).first()
    
    return render_template("first.html",user=user,cont=cont)

@app.route("/logout",methods=["GET"])
def logout():

    logout_user()
    return render_template("enterance.html")

if __name__=="__main__":
    app.run(debug=True)



