from flask import Flask

papp = Flask(__name__)

@papp.route('/')
def hello():
    return '<h1> Hello</h1>'