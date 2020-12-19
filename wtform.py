from flask_wtf import  FlaskForm
from markupsafe import Markup
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired,  Length, EqualTo, Email, ValidationError
from models import User
from passlib.hash import pbkdf2_sha256


""" def invalid_credentials(form, field):
    #Username password check 
    #because of the password area that contains invoker,
    #we can have the field as password.form is also passed
    #by the classs it is invoked by. 

    usernm_ent = form.username.data
    psw_ent = field.data
    usern_ob = User.query.filter_by(username=usernm_ent).first()
    if usern_ob is None:
        raise ValidationError("Username or password is incorrectdd")
    
    elif psw_ent!= usern_ob.password:
        raise ValidationError("Username or password is incorrect")
 """

class RegForm(FlaskForm):
    """Reg Form"""

    username = StringField('username_label',
        validators=[InputRequired(message="You need to enter a username."),
                    Length(min=4,max=50, message="The limits for the username are between 4 and 50.")])
    
    name = StringField("name_label",  validators=[InputRequired("Please enter your name.")])
    surname = StringField("surname_label",  validators=[InputRequired("Please enter your surname.")])
    email = StringField("email_label",  validators=[InputRequired("Please enter your email address."), Email("This field requires a valid email address")])

    password = PasswordField('password_label',validators=[InputRequired(message="You need to enter a password."),
                    Length(min=1,max=50, message="The limits for the password are between 1 and 50.")])
    
    confirm_pwd = PasswordField('confirm_pwd_label',validators=[InputRequired(message="Confirm Password"),EqualTo('password',message="Passwords need to match.")])

    submit_button = SubmitField('Create the account')


    #validate_ func automaticly invoked.    
    def validate_username(self, username):
        usern_ob = User.query.filter_by(username=username.data).first()
        if usern_ob:
            raise ValidationError("This username is being used. ")
    
    def validate_email(self, email):
        usere_ob = User.query.filter_by(email=email.data).first()
        if usere_ob:
            raise ValidationError("This email is being used. ")
    

class LogForm(FlaskForm):

    """Login Form"""

    username = StringField('username_label',
        validators=[InputRequired(message="You need to enter a username.")
            ])
    
    password = PasswordField('password_label',validators=[InputRequired(message="You need to enter a password.")])

    submit_button = SubmitField('Giriş')
    
    
    #validate_ func automaticly invoked.    
    def validate_username(self, username):
        usern_ob = User.query.filter_by(username=username.data).first()
        
        if usern_ob is None:

            raise ValidationError("Username or password is incorrect ")
    
    def validate_password(form,field):
        usern_ob = User.query.filter_by(username=form.username.data).first()
        if not pbkdf2_sha256.verify(field.data,usern_ob.password):
            raise ValidationError("Username or password is incorrect")
     