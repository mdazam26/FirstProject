from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# first route
@app.route("/")
def welcome():
    return "hello world"


# add user_controller file to app.py
from controller import user_controller

if __name__ == "__main__":
    app.run(debug=True)
