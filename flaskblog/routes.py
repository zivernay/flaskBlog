from flaskblog import app, bcrypt, db
from flask import redirect , request #imports redirect method from flask 
from flask import render_template #Jinja 2  engine for rendering teplates
from flask import flash #diplays one time messages
from flask import url_for #creates links for routing
from flaskblog.forms import RegistrationForm, Login, MoreInfo, UpadateAccountForm, NewPost
from flaskblog.models import User, Post
from flask_login import login_user, logout_user #login function that takes user object
from flask_login import current_user, login_required
import secrets #to genrate a random hex used as file names e.g images
import os #used to get file extensions
from PIL import Image #to handle images like resizing to save space


@app.route("/") #setting up the routes/ url which run the function
@app.route("/home")
def home():
    posts = Post.query.all()
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
            flash('Incorrect email and password!. Check your details')
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

def save_image(form_picture):
    random_hex = secrets.token_hex(10)
    _, f_ext = os.path.splitext(form_picture.filename) #getting the file ext from file
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/image_files', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route("/account", methods=["POST", "GET"])
@login_required
def account():
    form = UpadateAccountForm()
    if form.validate_on_submit():
        if form.image_file.data:
            picture_fn = save_image(form.image_file.data)
            current_user.image_file = picture_fn
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Username and Email updated!", "success")
        return redirect(url_for("account"))

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email    
    image = url_for('static', filename=f"image_files/{current_user.image_file}")
    return render_template("account.html", title="Account", image_file=image, form=form)

@app.route("/post/new", methods=["POST", "GET"])
@login_required
def post_new():
    form = NewPost()
    if form.is_submitted() and form.validate():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Content Posted.", "success")
        return redirect(url_for("home"))
    return render_template("new_post.html", title="New Post", form=form)
