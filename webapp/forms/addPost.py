from wtforms import  StringField, TextAreaField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_wtf.file import FileField


class AddPostForm (FlaskForm):
    heading = StringField("Enter Heading: ", validators=[DataRequired()])
    postImage = FileField("Enter Image: ", validators=[DataRequired()])
    postContent = TextAreaField("Enter Post: ", validators=[DataRequired()])
    submit = SubmitField()