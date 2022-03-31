from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():

    time_now = datetime.now().strftime('%H:%M:%S')


if __name__ == '__main__':
    app.run() 
