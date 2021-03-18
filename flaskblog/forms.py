from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Optional, ValidationError
from flaskblog.models import User
from flaskblog import db

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField('email', validators= [DataRequired(),Length(min=3, max=60), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=32)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("username already exists!. Please try a different one.")
    
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("email already exists!. Please try signing in")
        
    '''basic structure of custom validators
    def validate_fieldname(self, fieldname):
        if condition
            raise ValidationError(message="...")
        '''

class Login(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(message="isai chaiyo vaDoma")])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Sign In")

class MoreInfo(FlaskForm):
    dob = DateField("date of birth",format="%Y %B %d %H", validators=[DataRequired()])
    gender = SelectField("gender", choices=["M", "F", "Zvimwewo"])
    choices = SelectMultipleField("nationality", choices=["Zimbabwean", "Southern A", "bATSWANA"])
