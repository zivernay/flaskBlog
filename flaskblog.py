from flask import Flask  #flaks class 
from flask import redirect  #imports redirect method from flask 
from flask import render_template # Jinja 2  engine for rendering teplates
from flask import flash # diplays one time messages
from flask import url_for # creates links for routing
from forms import RegistrationForm, Login, MoreInfo
from flask_sqlalchemy import SQLAlchemy #import the SQL class

from datetime import datetime
app = Flask(__name__) 

app.config['SECRET_KEY'] = '1'
app.config['SQLACHEMY_DATABASE_URL'] = "sqlite:///site.db"
db = SQLAlchemy(app) #instatiating the db

class User(db.Model):
    id = db.Column(db.Integer,nullable=False, primary_key=True, unique=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    image_file  = db.Column(db.String(20), default="default.jpg")
    password = db.Column(db.String(60), nullable=True)

    posts = db.relationship("Post", backref="author", lazy = True)

    def __repr__(self):
        return f"User({self.username}, {self.id}, {self.image_file})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.date_posted})"



posts = [
    {
        'author': 'AD Zivanai',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/") #setting up the routes/ url which run the function
@app.route("/home")
def home():
    return render_template("home.html", posts = posts)

@app.route("/about")
def about():
    return render_template("about.html", title = "Doma")

message1 = 'form successfully submitted for '
category = 'success'  

@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(message1 + str(form.f_name.data), category)
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = Login()
    print('ran')
    if form.validate_on_submit():
        print('ran loop')
        flash(f"congrats {form.email.data} you have logged in!", "success")
        return redirect(url_for("home"))
    return render_template("login.html", form=form)

@app.route("/more", methods=["POST", "GET"])
def more():
    form = MoreInfo()
    if form.is_submitted() and form.validate():
        flash(f"successfully added more information", "success")
        return redirect(urlfor("home"))
    return render_template("more.html")


if __name__ == "__main__":
    app.run(debug=True)
