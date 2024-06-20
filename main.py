from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/register')
def register_page():
    return "<h1>Hello mridul</h1>"