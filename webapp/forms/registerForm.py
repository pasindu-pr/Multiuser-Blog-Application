from wtforms import  StringField,SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from .loginForm import LoginForm
from flask_wtf.file import FileField

class RegisterForm(LoginForm):
    name = StringField("Enter Full Name: ", validators=[DataRequired()])
    userImage = FileField("Upload Profile Image: ", validators=[DataRequired()])
    confirmPassword = PasswordField("Confirm Password: ", validators=[DataRequired(),EqualTo('password', message='Both Password and Confirm Password must match')])
    submit = SubmitField("Register")