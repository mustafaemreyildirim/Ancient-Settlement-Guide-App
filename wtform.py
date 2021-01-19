from flask_wtf import  FlaskForm
from markupsafe import Markup
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.fields.simple import FileField
from wtforms.validators import InputRequired,  Length, EqualTo, Email, ValidationError
from models import User, Contributor
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
    """User Reg Form"""
    style={'class': 'input is-medium','style':'font-family: Quicksand'}

    username = StringField('username_label',
        validators=[InputRequired(message="You need to enter a username."),
                    Length(min=4,max=50, message="The limits for the username are between 4 and 50.")],render_kw=style)
    
    name = StringField("name_label",  validators=[InputRequired("Please enter your name.")],render_kw=style)
    surname = StringField("surname_label",  validators=[InputRequired("Please enter your surname.")],render_kw=style)
    email = StringField("email_label",  validators=[InputRequired("Please enter your email address."), Email("This field requires a valid email address")],render_kw=style)

    password = PasswordField('password_label',validators=[InputRequired(message="You need to enter a password."),
                    Length(min=1,max=50, message="The limits for the password are between 1 and 50.")],render_kw=style)
    
    confirm_pwd = PasswordField('confirm_pwd_label',validators=[InputRequired(message="Confirm Password"),EqualTo('password',message="Passwords need to match.")],render_kw=style)

    submit_button = SubmitField('Create the account',render_kw={'button class': 'button is-block is-info is-medium is-fullwidth','style':'font-family: Quicksand;font-weight:bold'})

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

    """ User Login Form"""
    style={'class': 'input is-medium','style':'font-family: Quicksand'}

    username = StringField('username_label',
        validators=[InputRequired(message="You need to enter a username.")
            ],render_kw=style)
    
    password = PasswordField('password_label',validators=[InputRequired(message="You need to enter a password.")],render_kw=style)
    submit_button = SubmitField('Login',render_kw={'button class': 'button is-block is-info is-large is-fullwidth','style':'font-family: Quicksand;font-weight:bold'})
    
    
    #validate_ func automaticly invoked.    
    def validate_username(self, username):
        usern_ob = User.query.filter_by(username=username.data).first()
        
        if usern_ob is None:

            raise ValidationError("Username or password is incorrect")
    
    def validate_password(form,field):
        usern_ob = User.query.filter_by(username=form.username.data).first()
        if usern_ob is None:

            raise ValidationError("Username or password is incorrect")
    
        if not pbkdf2_sha256.verify(field.data,usern_ob.password):
            raise ValidationError("Username or password is incorrect")
     


class ContRegForm(FlaskForm):
    """User Reg Form"""
    style={'class': 'input is-medium','style':'font-family: Quicksand'}

    username = StringField('username_label',
        validators=[InputRequired(message="You need to enter a username."),
                    Length(min=4,max=50, message="The limits for the username are between 4 and 50.")],render_kw=style)
    
    name = StringField("name_label",  validators=[InputRequired("Please enter your name.")],render_kw=style)
    surname = StringField("surname_label",  validators=[InputRequired("Please enter your surname.")],render_kw=style)
    email = StringField("email_label",  validators=[InputRequired("Please enter your email address."), Email("This field requires a valid email address")],render_kw=style)
    university = StringField("university_label",  validators=[InputRequired("Please enter your university name.")],render_kw=style)
    researcharea = StringField("researcharea_label",  validators=[InputRequired("Please enter your research area.")],render_kw=style)

    password = PasswordField('password_label',validators=[InputRequired(message="You need to enter a password."),
                    Length(min=1,max=50, message="The limits for the password are between 1 and 50.")],render_kw=style)
    
    confirm_pwd = PasswordField('confirm_pwd_label',validators=[InputRequired(message="Confirm Password"),EqualTo('password',message="Passwords need to match.")],render_kw=style)

    submit_button = SubmitField('Create the account',render_kw={'button class': 'button is-block is-info is-medium is-fullwidth','style':'font-family: Quicksand;font-weight:bold'})

    #validate_ func automaticly invoked.    
    def validate_username(self, username):
        usern_ob = Contributor.query.filter_by(username=username.data).first()
        if usern_ob:
            raise ValidationError("This username is being used. ")
    
    def validate_email(self, email):
        usere_ob = Contributor.query.filter_by(email=email.data).first()
        if usere_ob:
            raise ValidationError("This email is being used. ")
    

class ContLogForm(FlaskForm):

    """ User Login Form"""
    style={'class': 'input is-medium','style':'font-family: Quicksand'}

    username = StringField('username_label',
        validators=[InputRequired(message="You need to enter a username.")
            ],render_kw=style)
    
    password = PasswordField('password_label',validators=[InputRequired(message="You need to enter a password.")],render_kw=style)
    submit_button = SubmitField('Login',render_kw={'button class': 'button is-block is-info is-large is-fullwidth','style':'font-family: Quicksand;font-weight:bold'})
    
    
    #validate_ func automaticly invoked.    
    def validate_username(self, username):
        usern_ob = Contributor.query.filter_by(username=username.data).first()
        
        if usern_ob is None:

            raise ValidationError("Username or password is incorrect")
    
    def validate_password(form,field):
        usern_ob = Contributor.query.filter_by(username=form.username.data).first()
        if usern_ob is None:

            raise ValidationError("Username or password is incorrect")
    
        if not pbkdf2_sha256.verify(field.data,usern_ob.password):
            raise ValidationError("Username or password is incorrect")

class AnSetForm(FlaskForm):
    
    
    style={'class': 'input-field','style':'font-family: Quicksand; box-sizing: border-box;-webkit-box-sizing: border-box;-moz-box-sizing: border-box;border: 1px solid #C2C2C2; box-shadow: 1px 1px 4px ;#EBEBEB;-moz-box-shadow: 1px 1px 4px #EBEBEB;-webkit-box-shadow: 1px 1px 4px #EBEBEB;border-radius: 3px;-webkit-border-radius: 3px;-moz-border-radius: 3px; padding: 7px; outline: none;'}
    cityname = StringField('cityname_label',
        validators=[InputRequired(message="You need to enter a cityname.")
            ],render_kw=style)

    location = StringField('location_label',
        validators=[InputRequired(message="You need to enter a location.")
            ],render_kw=style)

    region = StringField('region_label',
        validators=[InputRequired(message="You need to enter a region.")
            ],render_kw=style)

    civilization = StringField('civilization_label',
        validators=[InputRequired(message="You need to enter a civilization.")
            ],render_kw=style)

    knownperson = StringField('knownperson_label',
        validators=[InputRequired(message="You need to enter a known person from the city.")
            ],render_kw=style)

    description = TextAreaField('description_label',
        validators=[InputRequired(message="You need to enter a description.")
            ],render_kw={'class': 'textarea-field','style':'font-family: Quicksand; box-sizing: border-box;-webkit-box-sizing: border-box;-moz-box-sizing: border-box;border: 1px solid #C2C2C2; box-shadow: 1px 1px 4px ;#EBEBEB;-moz-box-shadow: 1px 1px 4px #EBEBEB;-webkit-box-shadow: 1px 1px 4px #EBEBEB;border-radius: 3px;-webkit-border-radius: 3px;-moz-border-radius: 3px; padding: 7px; outline: none;height: 100px;width: 68%;'})

    img = FileField('img_label',
        validators=[InputRequired(message="You need to enter a description.")])

    submit_button = SubmitField('Submit',render_kw={'button class': 'button ','style':'font-family: Quicksand;font-weight:bold;border: none;padding: 8px 15px 8px 15px;background: #FF8500;color: #fff; box-shadow: 1px 1px 4px #DADADA;-moz-box-shadow: 1px 1px 4px #DADADA;-webkit-box-shadow: 1px 1px 4px #DADADA; border-radius: 3px;-webkit-border-radius: 3px;-moz-border-radius: 3px;'})
