from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Optional

class RegistrationForm(FlaskForm):
    l_name = StringField('last name', validators=[DataRequired(), Length(min=3, max=30)])
    f_name = StringField('first name', validators=[DataRequired(), Length(min=3, max=30)])
    s_name = StringField('Second name', validators=[Optional(), Length(min=3, max=30)])

    #email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Sign Up')
