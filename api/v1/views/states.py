#!/usr/bin/python3
""""states"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from datetime import datetime
import uuid


@app_views.route('/states/', methods=['GET'])
def list_all_states():
    """"retrieves a list of all states data"""
    states = [state.to_dict() for state in storage.all("State").values()]
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state_by_id(state_id):
    """"retrieves a list of all states data"""
    states = storage.all("State").values()
    single_state = [state.to_dict()
                    for state in states if state.id == state_id]
    if single_state == []:
        abort(404)
    return jsonify(single_state)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    states = storage.all("State").values()
    single_state = [state.to_dict()
                    for state in states if state.id == state_id]
    if single_state == []:
        abort(404)
    single_state.remove(single_state[0])
    for state in states:
        if state.id == state_id:
            storage.delete(state)
            storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'])
def create_states():
    """"add new states"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    states = []
    new_states = State(name=request.json['name'])
    storage.new(new_states)
    storage.save()
    states.append(new_states.to_dict())
    return jsonify(states[0]), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_states(state_id):
    """"update existing states"""
    states = storage.all("State").values()
    single_state = [state.to_dict()
                    for state in states if state.id == state_id]
    if single_state == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    single_state[0]['name'] = request.json['name']
    for state in states:
        if state.id == state_id:
            state.name = request.json['name']
    storage.save()
    return jsonify(single_state[0]), 200
