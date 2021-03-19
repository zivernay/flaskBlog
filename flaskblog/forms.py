from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Optional, ValidationError, EqualTo
from flaskblog.models import User
from flaskblog import db
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField('email', validators= [DataRequired(),Length(min=3, max=60), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=32)])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo("password", message="zvakasiyana")])
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

class UpadateAccountForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField('email', validators= [DataRequired(),Length(min=3, max=60), Email()])
    image_file = FileField("Upload Profile Picture", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if current_user.username != username.data:
            if User.query.filter_by(username=username.data).first():
                raise ValidationError("username already exists!. Please try a different one.")

    def validate_email(self, email):
        if current_user.email != email.data:
            if User.query.filter_by(email=email.data).first():
                raise ValidationError("email already exists!. Please try signing in")