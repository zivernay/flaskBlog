from flask import Flask  #flaks class 
from flask import redirect  #imports redirect method from flask 
from flask import render_template # Jinja 2  engine for rendering teplates
from flask import flash # diplays one time messages
from flask import url_for # creates links for routing
from forms import RegistrationForm
app = Flask(__name__) 

app.config['SECRET_KEY'] = '1'
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
    else:
        flash("invalid form !", category="danger")
    return render_template('register.html', title='register', form=form)


if __name__ == "__main__":
    app.run(debug=True)
