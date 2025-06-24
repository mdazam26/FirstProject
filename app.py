from flask import Flask
from login_user import Fetch

app = Flask(__name__)




@app.route('/')
def welcome():
    return 'hello world222'

@app.route("/fetch")
def fetch_user():
    f = Fetch()
    result = f.get_users()
    return result




