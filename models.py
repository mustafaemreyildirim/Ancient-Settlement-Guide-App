from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

    # define this func to override predefined get_id()
    # because it looks for "id", in db this column is called
    # as "userid". Hence it is implemented. 
    def get_id(self):
        return (self.userid)

class Contributor(UserMixin, db.Model):
    """User Model"""

    __tablename__ = "user"
    contid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255),unique=True, nullable=False)
    createdate = db.Column(db.DateTime(timezone=True), nullable=False)

    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    university = db.Column(db.String(255), nullable=False)
    researcharea = db.Column(db.String(255), nullable=False)


    # define this func to override predefined get_id()
    # because it looks for "id", in db this column is called
    # as "userid". Hence it is implemented. 
    def get_id(self):
        return (self.contid)
