from flaskblog import app, bcrypt, db
from flask import redirect , request #imports redirect method from flask 
from flask import render_template #Jinja 2  engine for rendering teplates
from flask import flash #diplays one time messages
from flask import url_for #creates links for routing
from flaskblog.forms import RegistrationForm, Login, MoreInfo
from flaskblog.models import User
from flask_login import login_user, logout_user #login function that takes user object
from flask_login import current_user, login_required

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
 

@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        passHash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=passHash)
        db.session.add(user)
        db.session.commit()
        flash('Account successfully created. You can now logIn' , "success")
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = Login()
    print('ran')
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f"congrats {form.email.data} you have logged in!", "success")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flask('Incorrect email and password!. Check your details')
    return render_template("login.html", form=form)

@app.route("/more", methods=["POST", "GET"])
def more():
    form = MoreInfo()
    if form.is_submitted() and form.validate():
        flash(f"successfully added more information", "success")
        return redirect(urlfor("home"))
    return render_template("more.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")