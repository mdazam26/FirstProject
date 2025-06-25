from flask import Flask , request
from flask_cors import CORS 
app = Flask(__name__)
# CORS(app) 

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def welcome():

    return 'hello world'


from controller import user_controller

if __name__ == '__main__':
    app.run(debug=True)
