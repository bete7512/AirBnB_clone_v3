#!/usr/bin/python3
""""users"""
from crypt import methods
from api.v1.views import app_views
from flask import jsonify,abort,request
from models import storage
from models.user import User
from datetime import datetime
import uuid

@app_views.route('/users/',methods=['GET'])
def list_users():
    """"list users """
    users = [user.to_dict() for user in storage.all("User").values()]
    return jsonify(users)
@app_views.route('/users/<user_id>',methods=['GET'])
def get_user_by_id(user_id):
    """"fetch user data by id """
    users = storage.all("User").values()
    user = [user.to_dict() for user in users if user.id == user_id]
    if user == []:
        abort(404)
    return jsonify(user)
@app_views.route('/users/user_id>',methods=['DELETE'])
def delete_user_by_id(user_id):
    """"delete user by thier Id """
    users = storage.all("User").values()
    user = [user.to_dict() for user in users if user.id == user_id]
    if user == []:
        abort(404)
    user.remove
