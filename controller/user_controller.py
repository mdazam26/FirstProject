from app import app
from flask import request
from model.user_model import User_model

model_obj = User_model()

@app.route('/user/signup', methods=['POST'])
def user_signup():
    data = request.get_json()
    model_obj = User_model()
    return model_obj.user_signup_logic(data)

@app.route('/user/login',methods=['POST'])
def user_login():
    data = request.get_json()
    model_obj = User_model()
    return model_obj.user_login_logic(data)


@app.route("/user/getall" ,methods=['POST'])
def user_getall():
    data = request.get_json()
    model_obj = User_model()
    return model_obj.user_getall_logic(data)

@app.route("/user/update", methods=['PUT'])
def user_update():
    data = request.get_json()
    model_obj = User_model()
    return model_obj.user_update_logic(data)


@app.route("/user/delete/<int:id>", methods=['DELETE'])
def user_delete(id):
    data = request.get_json()
    model_obj = User_model()
    return model_obj.user_delete_logic(id)