from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

@app.route("/cool")
def html():
    return '''
    <html>
    <body style="background-color:black; color:blue"><h1>Cool</h1></body>
    </html>'''


""" if __name__ == "__main__":
    app.run(debug=True) """