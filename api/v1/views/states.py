#!/usr/bin/python3
"""
Module: states

This module defines the endpoints needed to perform CRUD operations
on the State object.

Endpoints:
    - GET '/states': Return a list of all State objects.
    - GET '/states/<state_id>': Return a specific State object.
    - DELETE '/states/<state_id>': Delete a specific State object.
    - POST '/states': Create a new State object.
    - PUT '/states/<state_id>': Update a specific State object.
"""

from api import classes
from api.v1.views import app_views
from flask import jsonify, abort, current_app, request


@app_views.route('/states', methods=['GET'])
def get_states():
    """Retrieve the list of State objects"""
    states = current_app.config.get('STORAGE').all(classes.get('State'))
    states_list = [state.to_dict() for state in states.values()]
    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Retrieve a State object"""
    storage = current_app.config.get('STORAGE')
    state = storage.all(classes.get('State')).get(f'State.{state_id}')
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Delete a State object"""
    storage = current_app.config['STORAGE']
    state = storage.all(classes.get('State')).get(f'State.{state_id}')
    if state:
        state.delete()
        storage.save()
    else:
        abort(404)
    return jsonify({})


@app_views.route('/states', methods=['POST'])
def create_state():
    """Delete a State object"""
    data = request.get_json()  # deserialize request body to object
    if not data:
        return jsonify(error="Not a JSON"), 400
    elif 'name' not in data:  # name property not present in the request body
        return jsonify(error="Missing name"), 400

    # create state object and save to database
    state = classes.get('State')(**data)
    state.save()
    return jsonify(state.to_dict()), 201  # return the newly created object


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """ """
    data = request.get_json()
    if not data:
        return eresponse(error="Not a JSON"), 400
    # ignore id, created_at and updated_at
    for key in ['id', 'created_at', 'updated_at']:
        data.pop(key, None)

    states = current_app.config['STORAGE'].all(classes.get('State'))
    state = states.get(f'State.{state_id}')
    if state:  # update object attributes
        for key, value in data.items():
            setattr(state, key, value)
        state.save()
    else:  # object not found
        abort(404)
    return jsonify(state.to_dict()), 200
