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
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})
