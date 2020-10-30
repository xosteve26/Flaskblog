from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User


class RegisterationForm(FlaskForm):
    username = StringField('Username',
     validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email', 
     validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=64)])

    confirm_password = PasswordField('Confirm-Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Whoa Whoa hold up there, it appears that this username is already taken. Please choose another one.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Whoa whoa hold up, it appears that this email is already taken. Please choose another one.')


class LoginForm(FlaskForm):

    email = StringField('Email', 
     validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=64)])

    remember = BooleanField('Remember - Me')

    submit = SubmitField('Login')
    


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
     validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email', 
     validators=[DataRequired(), Email()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:

            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Whoa Whoa hold up there, it appears that this username is already taken. Please choose another one.')
    def validate_email(self, email):
        if email.data != current_user.email:

            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Whoa whoa hold up, it appears that this email is already taken. Please choose another one.')


class RequestResetForm(FlaskForm):
    email = StringField('Email', 
     validators=[DataRequired(), Email()])

    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('This email is not associated with any account. Please Regiser for one')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=64)])

    confirm_password = PasswordField('Confirm-Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

