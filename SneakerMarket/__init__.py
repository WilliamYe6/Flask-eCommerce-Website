from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__) #initiates a flask instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sneaker.db' #allows the flask App to identify which db we are using
app.config['SECRET_KEY'] = '7e8a15d729c587e384be74d4' #extra form of security for registration and login forms (forms.html) 
db = SQLAlchemy(app) #initiates an instance of the class SQLAlchemy
bcrypt = Bcrypt(app) #helps hash passwords in our database
login_manager = LoginManager(app) #creates an instange of LoginManager Class
login_manager.login_view = "login" #redirects user to login page from home page
login_manager.login_message_category = "info"

from SneakerMarket import routes
from SneakerMarket import models