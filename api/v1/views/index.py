#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This script handles the routes suported
    by the blueprint previously created.
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', strict_slashes=False)
def api_status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def api_number_of_objs():
    classes = {"Amenity": "Amenity",
               "City": "City",
               "Place": "Place",
               "Review": "Review",
               "State": "State",
               "User": "User"}

    for key, value in classes.items():
        classes[key] = storage.count(value)
    return jsonify(classes)
