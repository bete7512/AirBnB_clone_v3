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
    amenities = [key.to_dict() for key in storage.all("Amenity").values]
    return jsonify(amenities)
@app_views('/<id>')
def get_amenity_by_id(id):
    """"fetch amenity by amenity ID"""
    amenities = storage.all("Amenity").values()