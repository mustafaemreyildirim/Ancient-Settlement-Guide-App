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



login = LoginManager(app)
login.init_app(app)
usr=0


@login.user_loader
def load_user(user_id):
    
    return get_user(user_id)

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
    
    
    
    global usr
    login_form = LogForm()
    if login_form.validate_on_submit():
        
        us_ret = get_user(login_form.username.data)
        #user=User.query.filter_by(username=login_form.username.data).first()
        
        login_user(us_ret)
        if current_user.is_authenticated: 
            usr=current_user.username
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
 

        cont = Cont_remade (username,hashed_pw,email,createdate,name,surname,university,researcharea)
        cont.insert()
        user = User_remade(username,hashed_pw,email,createdate,name,surname)
        user.insert()

        #db.session.add(cont)
        #db.session.add(user)
        #db.session.commit()
        return redirect(url_for('cont_login'))

    return render_template("reg_index.html",form=reg_form)


@app.route("/cont_login",methods=["GET", "POST"])
def cont_login():
    

    login_form = LogForm()
    global usr
    if login_form.validate_on_submit(): 
        us_ret = get_user(login_form.username.data)
        #user=User.query.filter_by(username=login_form.username.data).first()
        login_user(us_ret)
        if current_user.is_authenticated: 
            usr=current_user.username
            return redirect(url_for('cities'))
    
    return render_template("reg_login.html", form=login_form)


@app.route("/profile/<username>",methods=["GET", "POST"])
def profile(username):
    
    
    user = get_user(username)
    cont= get_cont(username)
    
    message=0
    if cont:
        message = 1
        return render_template("cont_profile.html",user=user,cont=cont,message = message)
    return render_template("profile.html",user=user,message=message)

@app.route("/add_cities", methods=["GET", "POST"])
def add_cities():
    

    set_form = AnSetForm()
    global usr
    if set_form.validate_on_submit():
        cityname = set_form.cityname.data
        location = set_form.location.data
        region = set_form.region.data
        civilization = set_form.civilization.data
        goldenage = set_form.goldenage.data
        knownperson = set_form.knownperson.data
        description = set_form.description.data
        img = set_form.img.data

        reg = get_reg(region)
        if reg==None:
            
            reg_add = Region_remade(region)
            reg_add.insert()
            


        kp = get_fp(knownperson)
        if kp==None: 
            kn_add = Knownp_remade(knownperson)
            kn_add.insert()
        

        civi = get_civi(civilization)
        if civi == None:
            civi_add = Civi_remade(civilization,goldenage,knownperson)
            civi_add.insert()
        
        loc = get_loc(location)
        if loc == None:
            loc_add = Location_remade(location,region)
            loc_add.insert()
        print("----------------------------------------->>>>",usr)
        aset = get_set(cityname)
        if aset == None:
            aset_add = AnSett_remade(cityname,usr,location,civilization,description,img)
            aset_add.insert()
        
        return redirect(url_for('cities'))

    return render_template("add_ancient_settlement.html",form=set_form)

@app.route("/add_paths", methods=["GET", "POST"])
def add_paths():
    

    path_form = PathForm()
    if path_form.validate_on_submit():
        pathname = path_form.pathname.data
        artifacts = path_form.artifacts.data
        civilization = path_form.civilization.data
        location = path_form.location.data
        pathimg = path_form.pathimg.data
        region = path_form.region.data
        knownperson = path_form.knownperson.data
        goldenage= path_form.goldenage.data

        reg = get_reg(region)
        if reg==None:
            
            reg_add = Region_remade(region)
            reg_add.insert()
        kp = get_fp(knownperson)
        if kp==None:
            kp_add=Knownp_remade(knownperson)
            kp_add.insert()
        cv = get_civi(civilization)
        if cv == None:
            cv_add = Civi_remade(civilization,goldenage,knownperson)
            cv_add.insert()
        
        lk = get_loc(location)
        if lk== None:
            lk_add= Location_remade(location,region)
            lk_add.insert()
        pt = get_path(pathname)
        if pt == None:
            pt_add = Path_remade(pathname,artifacts,civilization,location,pathimg)
            pt_add.insert()

        return redirect(url_for('cities'))

    return render_template("add_paths.html",form=path_form)


@app.route("/cities",methods=["GET", "POST"])
def cities():
    global usr
    
    user = get_user(usr)
    cont = get_cont(usr)
    ls = bring_all_cities()
    ms = bring_all_paths()
    mlen = len(ms)

    leng = len(ls)
  
    return render_template("first.html",user=user,cont=cont,ls=ls,leng=leng,ms=ms,mlen=mlen)

@app.route("/logout",methods=["GET"])
def logout():

    logout_user()
    return render_template("enterance.html")

if __name__=="__main__":
    app.run(debug=True)



