from flask import Flask , request
from login_user import Fetch

app = Flask(__name__)




@app.route('/')
def welcome():

    return 'hello world'



# @app.route("/fetch")
# def fetch_user():
#     f = Fetch()
#     result = f.get_users()
#     return result

# from controller import *
from controller import user_controller

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/update/<id>', methods=['POST'])
# def update(id):
#     f = Fetch()
#     result = f.update_user(id,request.form)
#     return result   

# @app.route('/add',methods=['POST'])
# def add():
#     try:
#         try:
#             f = Fetch()
#         except:
#             return " object not created"
#         # result = f.add_user(request.form)
#         return f.add_user(request.form)   
#     except:
#         return "route error"