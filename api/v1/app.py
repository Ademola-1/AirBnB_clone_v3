#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is the entry point for managing all blueprints"""
from flask import Flask, Response
from models import storage
from api.v1.views import app_views
import json


# A register of the main flask app
app = Flask(__name__)
# A register of a blueprint the main flask app.
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found_page(error):
    four_0_four_page = json.dumps({"error": "Not found"}, indent=2)
    return Response(
            four_0_four_page,
            status=404,
            content_type='application/json')


@app.teardown_appcontext
def tear_down(exception):
    """
        tear_down: this function closes the db/storage
        Argunments:
            exception (Exception): will contain an exception.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
