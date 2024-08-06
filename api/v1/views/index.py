#!/usr/bin/python3
# api/v1/views/index.py

"""
This module defines the view for the API status endpoint.
"""

from flask import jsonify, make_response
"""
Module: index

Description:
    This module defines the routes for the API version 1.
    It handles the routing and endpoints necessary for the application's
    API functionality.

Endpoints:
    '/status' - Returns the status of the API
"""
from api.v1.views import app_views
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
    """
    Handle 404 errors by returning a JSON response with a 404 status code.
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})

    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Counts and returns the number of objects of the mapped classs"""
    from api import classes
    from models import storage

    def cls_name_plural(name):
        """convert mapped class name to it plural form"""
        name = name.lower()
        return name.replace('y', 'ies') if name.endswith('y') else name + 's'

    stats_dict = {cls_name_plural(cls): storage.count(cls) for cls in classes}
    return jsonify(stats_dict)
