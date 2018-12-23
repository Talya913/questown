from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, BooleanField, ValidationError
from questown.models import Users

class RegistrationForm(FlaskForm):
    username = StringField('Username', [
        validators.data_required(),
        validators.length(min=2, max=15)
    ])
    name = StringField('Name', [
        validators.data_required()
    ])
    email = StringField('Email', [
        validators.data_required(),
        validators.email()
    ])
    password = PasswordField('Password', [
        validators.data_required(),
        validators.length(min=6, max=20)
    ])
    confirm_password = PasswordField('Confirm Password', [
        validators.data_required(),
        validators.equal_to('password')
    ])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Sorry, that username is already taken')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Sorry, that email is already taken')


class LoginForm(FlaskForm):
    email = StringField('Email', [
        validators.data_required(),
        validators.email()
    ])
    password = PasswordField('Password', [
        validators.data_required()
    ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
