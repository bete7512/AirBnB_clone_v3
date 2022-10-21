#!/usr/bin/python3
""""cities fetching"""
from datetime import datetime
from api.v1.views import app_views

from flask import jsonify,abort,request
from models import storage
from models.city import City
from models.state import State
from datetime import datetime
import uuid

@app_views.route('/states')