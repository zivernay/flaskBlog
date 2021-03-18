from flask import Flask  #flaks class 
from flask_sqlalchemy import SQLAlchemy #import the SQL class
import os

app = Flask(__name__) 
app.config['SECRET_KEY'] = '1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(os.getcwd(), 'flaskblog\\site.db')
db = SQLAlchemy(app) #instatiating the db

from flaskblog import routes