#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This script handles the routes suported
    by the blueprint previously created.
"""
from flask import Response
from api.v1.views import app_views
from models import storage
import json


@app_views.route('/status', strict_slashes=False)
def api_status():
    status_ok = json.dumps({"status": "OK"}, indent=2)
    return Response(status_ok, content_type='application/json')


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
    formatted_output = json.dumps(classes, indent=2)
    return Response(formatted_output, content_type='application/json')
