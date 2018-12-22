from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, BooleanField


class RegistrationForm(FlaskForm):
    username = StringField('Username',[
        validators.data_required(),
        validators.length(min=2, max=15)
    ])
    name = StringField('Name', [
        validators.data_required()
    ])
    surname = StringField('Surname',[
        validators.data_required()
    ])
    email = StringField('Email',[
        validators.data_required(),
        validators.email()
    ])
    password = PasswordField('Password', [
        validators.data_required()
    ])
    confirm_password = PasswordField('Confirm Password', [
        validators.data_required(),
        validators.equal_to('password')
    ])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',[
        validators.data_required(),
        validators.email()
    ])
    password = PasswordField('Password', [
        validators.data_required()
    ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')