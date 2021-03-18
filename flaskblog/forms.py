from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Optional

class RegistrationForm(FlaskForm):
    l_name = StringField('last name', validators=[DataRequired(), Length(min=3, max=30)])
    f_name = StringField('first name', validators=[DataRequired(), Length(min=3, max=30)])
    s_name = StringField('Second name', validators=[Optional(), Length(min=3, max=30)])
    submit = SubmitField('Sign Up')

class Login(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(message="isai chaiyo vaDoma")])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Sign In")

class MoreInfo(FlaskForm):
    dob = DateField("date of birth",format="%Y %B %d %H", validators=[DataRequired()])
    gender = SelectField("gender", choices=["M", "F", "Zvimwewo"])
    choices = SelectMultipleField("nationality", choices=["Zimbabwean", "Southern A", "bATSWANA"])
