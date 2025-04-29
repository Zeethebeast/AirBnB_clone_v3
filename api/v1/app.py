#!/usr/bin/python3
"""
Module: app

"""
This module sets up the Flask application for the API.
It registers the blueprint and handles teardown of the database session.
"""

Description:
    This module sets up and configures a Flask application instance with
    various endpoints.

Functions:
    teardown_db() -> None
        Deletes the current database session and creates a new one.

Notes:
    For more information about the routes, see the /api/v1/views/ directory.
"""
from flask import Flask
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False
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

    
    """Close the storage on teardown"""
    app.config['STORAGE'].close()


if __name__ == "__main__":
    from models import storage

    app.config['STORAGE'] = storage
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True, debug=True)
