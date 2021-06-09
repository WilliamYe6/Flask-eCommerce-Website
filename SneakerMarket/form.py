from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from SneakerMarket.models import User

#Class created for Registration of users
class RegistrationForm(FlaskForm):

    #method to check for duplicate usernames
    def validate_username(self, usernameCheck):
        user = User.query.filter_by(username = usernameCheck.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
    #method to check for duplicate emails
    def validate_email_address(self, emailCheck):
        email_address= User.query.filter_by(email = emailCheck.data).first()
        if email_address:
            raise ValidationError('Email address already exists! Please try a different email')

    #attributes for the class Registration Form
    username = StringField(label = 'User Name:', validators=[Length(min=2, max= 30),DataRequired()])
    email_address = StringField(label = 'Email Address:', validators = [Email(),DataRequired()])
    password = PasswordField(label = 'Password:', validators=[Length(min=6),DataRequired()])
    confirm_password = PasswordField(label = 'Confirm Password:', validators = [EqualTo('password'),DataRequired()])
    register = SubmitField(label = 'Create Account')

#Class created for the Login of users
class LoginForm(FlaskForm):
    #attributes of login form
    username = StringField(label = "User Name:", validators = [DataRequired()])
    password = PasswordField(label = 'Password:', validators = [DataRequired()])
    login = SubmitField(label = 'Login')

#Class to allow users to purchase sneakers  
class PurchaseSneaker(FlaskForm):
    purchase = SubmitField(label = 'Purchase')

#Class to allow users to sell sneakers
class SellSneaker(FlaskForm):
    sell = SubmitField(label = 'Sell')