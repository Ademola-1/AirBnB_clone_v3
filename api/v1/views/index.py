#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This script handles the routes suported
    by the blueprint previously created.
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def api_status():
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', strict_slashes=False)
def api_stats():
    pass
