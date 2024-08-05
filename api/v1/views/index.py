#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This script handles the routes suported
    by the blueprint previously created.
"""
from api.v1.views import app_views
from models import storage
import json


@app_views.route('/status', strict_slashes=False)
def api_status():
    return json.dumps({"status": "OK"}, indent=2)


@app_views.route('/stats', strict_slashes=False)
def api_number_of_objs():
    classes = {"amenities": "Amenity",
               "cities": "City",
               "places": "Place",
               "reviews": "Review",
               "states": "State",
               "users": "User"}

    for key, value in classes.items():
        classes[key] = storage.count(value)
    return json.dumps(classes, indent=2)
