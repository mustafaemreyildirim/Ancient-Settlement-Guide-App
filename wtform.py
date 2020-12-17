from flask_wtf import  FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired,  Length, EqualTo, Email

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
