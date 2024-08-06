#!/usr/bin/python3
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
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns the status of the API"""
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
