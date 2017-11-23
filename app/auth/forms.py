from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Не выходить из системы.')
    submit = SubmitField('Авторизоваться')


class RegistrationForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Имя пользователя', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Имена пользователей должны иметь только буквы, цифры, точки или '
               'символы подчеркивания')])
    password = PasswordField('Пароль', validators=[
        DataRequired(), EqualTo('password2', message='Пароли должны совпадать.')])
    password2 = PasswordField('Подтвердите Пароль', validators=[DataRequired()])
    submit = SubmitField('Регистрация')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Электронная почта уже зарегистрирована.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Имя пользователя уже используется.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Старый пароль', validators=[DataRequired()])
    password = PasswordField('Новый пароль', validators=[
        DataRequired(), EqualTo('password2', message='Пароли должны совпадать.')])
    password2 = PasswordField('Подтвердите новый пароль',
                              validators=[DataRequired()])
    submit = SubmitField('Обновить пароль')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Сброс пароля')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Новый пароль', validators=[
        DataRequired(), EqualTo('password2', message='Пароли должны совпадать.')])
    password2 = PasswordField('Подтвердите Пароль', validators=[DataRequired()])
    submit = SubmitField('Сброс пароля')


class ChangeEmailForm(FlaskForm):
    email = StringField('Новый E-mail', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Обновить адрес электронной почты')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Электронная почта уже зарегистрирована.')
