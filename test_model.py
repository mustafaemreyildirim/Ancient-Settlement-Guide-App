from re import search
from flask import Flask, render_template, redirect
from flask.globals import current_app
from flask.helpers import url_for
from wtform import *
from models import *
from datetime import datetime
from flask_login import LoginManager, login_user,current_user, login_required, logout_user
from remade_model import *
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.secret_key="later"

app.config['SQLALCHEMY_DATABASE_URI']="postgres://zlcsxccctwmvdp:b2b27bc4b07b3b309412b7c51e0483eaea106ba964509517379406b3ae762bf4@ec2-34-194-198-238.compute-1.amazonaws.com:5432/d35q9ogcrt02v1"
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    """User Model"""

    __tablename__ = "user"

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255),unique=True, nullable=False)
    createdate = db.Column(db.DateTime(timezone=True), nullable=False)

    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)

    prfimg=db.Column(db.LargeBinary)

    # define this func to override predefined get_id()
    # because it looks for "id", in db this column is called
    # as "userid". Hence it is implemented. 
    def get_id(self):
        return (self.userid)
    def get_username(self):
        return (self.username)

login_form = LogForm()
user=User.query.filter_by(username=login_form.username.data).first()


""" con = psycopg2.connect("dbname='d35q9ogcrt02v1' user='zlcsxccctwmvdp' host='ec2-34-194-198-238.compute-1.amazonaws.com' password='b2b27bc4b07b3b309412b7c51e0483eaea106ba964509517379406b3ae762bf4'")
cur = con.cursor()

cur.execute("ROLLBACK")
con.commit()
a = 'yildirimmus16'
cur.execute("SELECT userid FROM \"user\"  WHERE \"username\" = '%s' LIMIT 1",a) 

rows = cur.fetchall()

print(rows) """

print(user)