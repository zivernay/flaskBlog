from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def  load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,nullable=False, primary_key=True, unique=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(60), nullable=False)
    image_file  = db.Column(db.String(20), default="default.jpg")
    password = db.Column(db.String(60), nullable=True)

    posts = db.relationship("Post", backref="author", lazy = True)

    def __repr__(self):
        return f"User({self.username}, {self.id} ,{self.email} ,{self.image_file})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.date_posted})"
