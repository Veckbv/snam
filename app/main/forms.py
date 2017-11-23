from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class ImageForm(FlaskForm):
    image = FileField(validators=[FileRequired()])
    submit = SubmitField('Отправить')
    
