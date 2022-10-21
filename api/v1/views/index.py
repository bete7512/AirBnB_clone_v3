#!/usr/bin/python3
"""first routes"""

from crypt import methods
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity 
from models.review import Review

classes = {"users":"User",
            "cities":"City",
            'reviews':"Review",
            'places':'Place',
            'amenities':'Amenity',
}
@app_views.route('/status',methods['GET'])
def status():
    """"""""
    return jsonify({'status':'OK'})
@app_views.route('/stats',methods=['GET'])
def count():
    ''''''''
    