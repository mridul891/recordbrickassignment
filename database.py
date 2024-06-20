from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb+srv://pandeym891:mridul891@cluster0.s0zigac.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

mongo = PyMongo(app)
