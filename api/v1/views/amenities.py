#!/usr/bin/python3
""""amenities"""
from api.v1.views import app_views
from flask import jsonify,abort,request
from models import storage
from models.amenity import Amenity
from datetime import datetime
import uuid

@app_views.route('/amenities',methods=['GET'])
def amenity_lists():
    """"amenity fetch"""
    amenities = 