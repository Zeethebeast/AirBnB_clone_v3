#!/usr/bin/python3
"""
Module: __init__.py

Description:
    This module creates a blueprint for the app, registering the API v1 routes.

Usage:
    Import this module to initialize the blueprint with the app's routes.

Blueprint:
    app_views - Blueprint for API v1 with the URL prefix '/api/v1'
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
