#!/usr/bin/python3
# api/v1/app.py

"""
This module sets up the Flask application for the API.
It registers the blueprint and handles teardown of the database session.
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown.
    This function is called when the request context is popped, 
    which means the function is executed when the application context ends.
    """
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)

    