from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from ..models import User, Role
from wtforms import ValidationError



class ImageForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    upload = FileField('Изображение', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Только изображение!')])
    submit = SubmitField('Отправить')
    

class EditProfileForm(FlaskForm):
    name = StringField('Настоящее имя', validators=[Length(0, 64)])
    location = StringField('Дислокация', validators=[Length(0, 64)])
    about_me = TextAreaField('Обо мне')
    submit = SubmitField('Редактировать')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Имя пользователя', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Имена пользователей должны иметь только буквы, цифры, точки или символы подчеркивания.')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Роль', coerce=int)
    name = StringField('Настоящее имя', validators=[Length(0, 64)])
    location = StringField('Дислокация', validators=[Length(0, 64)])
    about_me = TextAreaField('Обо мне')
    submit = SubmitField('Редактировать')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Электронная почта уже зарегистрирована.')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Имя пользователя уже используется.')