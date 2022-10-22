#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count('State')))

first_state_id = list(storage.all(State).values())[0].id
first_all_states = storage.all(State).values()
state_obj = [obj.to_dict() for obj in first_all_states if obj.id == first_state_id]
print(state_obj[0]['id'])
print("First state: {}".format(storage.get(State, first_state_id)))