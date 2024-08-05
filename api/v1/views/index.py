#!/usr/bin/python3
# api/v1/views/index.py

"""
This module defines the view for the API status endpoint.
"""

from api.v1.views import app_views
from flask import jsonify
from flask import make_response
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Returns the status of the API.

    This route returns a JSON object indicating the status of the API.
    """
    return jsonify({"status": "OK"}), 200

@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def count():
    """
    Retrieve the number of each object by type.
    """
    counts = storage.count()
    return jsonify(counts)

@app_views.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
