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
    list_users = [user.to_dict() for user in storage.all("User").values()]
