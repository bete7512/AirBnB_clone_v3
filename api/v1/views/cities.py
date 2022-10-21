#!/usr/bin/python3
""""cities fetching"""
from datetime import datetime
from api.v1.views import app_views

from flask import jsonify, abort, request
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
    all_cities = [key.to_dict() for key in storage.all("City").values()
                  if state_id == key.id]
    return jsonify(all_cities)


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def add_new_city(state_id):
    """"add new city"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    states = storage.all('State').values()
    current_state = [key.to_dict() for key in states if key.id == state_id]
    if current_state == []:
        abort(404)
    cities = []
    new_city = City(name=request.json['name'], state_id=state_id)
    storage.new(new_city)
    cities.append(new_city.to_dict())
    return jsonify(cities[0]), 201


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city_by_id(city_id):
    """"fetch cities by their Id"""
    all_cities = storage.all('City').values()
    single_city = [key.to_dict() for key in all_cities if key.id == city_id]
    if single_city == []:
        abort(404)
    return jsonify(single_city[0])


@app_views.route('/cities/<city_id>', methods=['POST'])
def delete_city_by_id(city_id):
    """"delete city from storage"""
    all_cities = storage.all("City").values()
    single_city = [key.to_dict() for key in all_cities if key.id == city_id]
    if single_city == []:
        abort(404)
    for key in all_cities:
        if key.id == city_id:
            storage.delete(key)
            storage.save()
            break
    return jsonify({}),200

@app_views.route