 # Import Flask class and request object for handling HTTP methods
from flask import Flask, request 
# Import CORS to allow cross-origin requests (useful for frontend-backend interaction)
from flask_cors import CORS


# Create an instance of the Flask app
app = Flask(__name__)
CORS(app)# Enables CORS


# first route
@app.route("/")
def welcome():
    return "hello world"


# add user_controller file to app.py
from controller import user_controller

if __name__ == "__main__": # Check if this script is run directly
    app.run(debug=True)  # Start the Flask development server debig mode enable
