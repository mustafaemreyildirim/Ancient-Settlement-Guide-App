from flask import Flask, render_template, redirect
from flask.globals import current_app
from flask.helpers import url_for
from wtform import *
from models import *
from datetime import datetime
from flask_login import LoginManager, login_user,current_user, login_required, logout_user

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

@app.route("/user_register",methods=["GET", "POST"])
def user_register():

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
        return redirect(url_for('user_login'))

    return render_template("index.html",form=reg_form)


@app.route("/user_login",methods=["GET", "POST"])
def user_login():

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
 

        cont = Contributor(username=username, password=hashed_pw, name=name, surname=surname,email=email,createdate=createdate,university=university,researcharea=researcharea)
        db.session.add(cont)
        db.session.commit()
        return redirect(url_for('cont_login'))

    return render_template("index.html",form=reg_form)


@app.route("/cont_login",methods=["GET", "POST"])
def cont_login():

    login_form = ContLogForm()

    if login_form.validate_on_submit():
        cont=Contributor.query.filter_by(username=login_form.username.data).first()
        login_user(cont)
        if current_user.is_authenticated:
            return redirect(url_for('cities'))
    
    return render_template("login.html", form=login_form)


@app.route("/cities",methods=["GET", "POST"])
def cities():

    if not current_user.is_authenticated:
        return "Please log into application!"
    

    return render_template("first.html")

@app.route("/logout",methods=["GET"])
def logout():

    logout_user()
    return render_template("enterance.html")

if __name__=="__main__":
    app.run(debug=True)



