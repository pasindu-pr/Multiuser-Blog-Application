from wtforms import  StringField, TextAreaField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_ckeditor import CKEditorField


class AddPostForm (FlaskForm):
    heading = StringField("Enter Heading: ", validators=[DataRequired()])
    postImage = FileField("Enter Image: ", validators=[DataRequired()])
    postContent = CKEditorField("Enter Post: ", validators=[DataRequired()])
    submit = SubmitField()