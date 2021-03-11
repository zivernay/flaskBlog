from flask import Flask  #flaks class 
from flask import render_template # Jinja 2  engine for rendering teplates
app = Flask(__name__) 

posts = [
    {
        'author': 'Corey Schafer',
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
def hello():
    return render_template("home.html", posts = posts)

@app.route("/about")
def html():
    return render_template("about.html", title = "Doma")


if __name__ == "__main__":
    app.run(debug=True)