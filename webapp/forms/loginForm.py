from wtforms import  StringField,SubmitField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField("Enter Email: ", validators=[DataRequired()])
    password = PasswordField("Enter Password: ", validators=[DataRequired()])
    submit = SubmitField("Login")