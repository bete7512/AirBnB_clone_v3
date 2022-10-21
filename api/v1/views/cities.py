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

@app_views.route('/states/<state_id>/cities')
def list_all_cities(state_id):
    all_states = storage.all("State").values()
    current_state = [key.to_dict() for key in all_states if key.id == state_id]
    if current_state == []:
        abort(404)
     all_cities = [key.to_dict() for key ] 
