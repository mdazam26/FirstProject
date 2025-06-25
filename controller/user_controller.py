from app import app
from flask import request
from model.user_model import User_model

model_obj = User_model()

@app.route('/user/signup', methods=['POST'])
def user_signup():
    model_obj = User_model()
    return model_obj.user_signup_logic(request.form)

@app.route('/user/login',methods=['PUT'])
def user_login():
    model_obj = User_model()
    return model_obj.user_login_logic(request.form)


@app.route("/user/getall")
def user_getall():
    model_obj = User_model()
    return model_obj.user_getall_logic()

@app.route("/user/update", methods=['PUT'])
def user_update():
    model_obj = User_model()
    return model_obj.user_update_logic(request.form)


@app.route("/user/delete/<int:id>", methods=['DELETE'])
def user_delete(id):
    model_obj = User_model()
    return model_obj.user_delete_logic(id)