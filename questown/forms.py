from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, BooleanField, ValidationError, widgets, SelectField, IntegerField
from questown.models import Users
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms_sqlalchemy.fields import QuerySelectField


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


class UpdateAccountForm(FlaskForm):
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
    gender = SelectField('Gender',
                         choices=['Male', 'Female', 'Not answered'])
    age = IntegerField('Age (in years)', [
        validators.NumberRange(min=1, max=100)
    ])
    about = StringField('About yourself', [
        validators.length(max=5000)
    ])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = Users.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Sorry, that username is already taken')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Sorry, that email is already taken')


#def choice_query():
 #   return Choice.query


#class GroupForm(FlaskForm):
 #   gender = QuerySelectField(query_factory=Choice.query, allow_blank=True)
    #age_min = QuerySelectField()
