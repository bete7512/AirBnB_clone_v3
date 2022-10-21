#!/usr/bin/python3
""""users"""
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
    user = [user.to_dict() for user in ]
