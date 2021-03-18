from flask import Flask  #flaks class 
from flask_sqlalchemy import SQLAlchemy #import the SQL class
import os
from flask_bcrypt import Bcrypt #hash generator and checker
from flask_login import LoginManager

app = Flask(__name__) 
app.config['SECRET_KEY'] = '1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(os.getcwd(), 'flaskblog\\site.db')
db = SQLAlchemy(app) #instatiating the db
bcrypt = Bcrypt(app) 
login_manager = LoginManager(app)
login_manager.login_view = 'login' #setting up login route for login required
login_manager.login_message_category = 'info'
from flaskblog import routes #imported after app to avoid circular import error