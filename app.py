from flask import Flask, render_template
from wtform import *
from models import *
from datetime import datetime, timedelta


app = Flask(__name__)
app.secret_key="later"

app.config['SQLALCHEMY_DATABASE_URI']="postgres://zlcsxccctwmvdp:b2b27bc4b07b3b309412b7c51e0483eaea106ba964509517379406b3ae762bf4@ec2-34-194-198-238.compute-1.amazonaws.com:5432/d35q9ogcrt02v1"
db = SQLAlchemy(app)

@app.route("/",methods=["GET", "POST"])
def index():

    reg_form = RegForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        name = reg_form.name.data
        surname = reg_form.surname.data
        email = reg_form.email.data
        password = reg_form.password.data
        createdate = datetime.now()


        usern_ob = User.query.filter_by(username=username).first()
        usere_ob = User.query.filter_by(email=email).first()

        if usere_ob :
            return "This email is being used. "
        
        elif usern_ob :
            return "This username is being used. " 

        user = User(username=username, password=password, name=name, surname=surname,email=email,createdate=createdate)
        db.session.add(user)
        db.session.commit()
        return "user is added into db!"

    return render_template("index.html",form=reg_form)

if __name__=="__main__":
    app.run(debug=True)

