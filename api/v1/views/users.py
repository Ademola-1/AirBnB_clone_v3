#!/usr/bin/python3
"""This script handles the routes suported
    by the blueprint previously created.
    Focusing majorly on handling all routes
    steaming from /amenities
"""
from flask import Response, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User
import json


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """
        get_all_users: a function that returns all the
                            users objects
        Returns: a JSON repr of containing all the objects
    """
    all_objs = []
    ret_obj = storage.all("User")
    for key, value in ret_obj.items():
        ret_objs = User(**value.__dict__)
        all_objs.append(ret_objs.to_dict())
    completed_json_dump = json.dumps(all_objs, indent=2)
    return Response(f"{completed_json_dump}\n", mimetype='application/json')


@app_views.route('/users/<user_id>',
                 methods=['GET'],
                 strict_slashes=False)
def get_user_by_id(user_id):
    """
        get_user_by_id: a function that retrieves a User given a matching id
        Argunments:
                an existing User ID is used for query purposes
        Return:
                The found object or a 404 if not found.
    """
    is_obj = storage.get(User, user_id)
    if is_obj is None:
        abort(404)
    ret_obj = json.dumps(User(**is_obj.__dict__).to_dict(), indent=2)
    return Response(f"{ret_obj}\n", mimetype='application/json')


@app_views.route('/users/<user_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_user_by_id(user_id):
    """
        delete_user_by_id: a function, when given an
        ID deletes the object in the DB
        Argunments: A User valid ID
        Return: An empty dict with status 200
    """
    is_obj = storage.get(User, user_id)
    if is_obj is None:
        abort(404)
    storage.delete(is_obj)
    storage.save()
    return Response(f"{json.dumps({}, indent=2)}\n",
                    status=200,
                    mimetype='application/json')


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """
        create_user: A function that creates a User obj
        Returns: The created User object
    """

    if not request.json:
        abort(400, "Not a JSON")
    if 'email' not in request.json:
        abort(400, "Missing email")
    if 'password' not in request.json:
        abort(400, "Missing password")

    posted_data = request.get_json()
    created_user = User(**posted_data)
    storage.new(created_user)
    storage.save()
    json_repr = json.dumps(User(**created_user.__dict__).to_dict(), indent=2)
    return Response(f"{json_repr}\n",  mimetype='application/json', status=201)


@app_views.route('/users/<user_id>',
                 methods=['PUT'],
                 strict_slashes=False)
def update_user(user_id):
    """
        update_user: a function that updates an existing User
        Argunments: a valid User ID
        Returns: The object with it's new update.
    """
    # These are the keys that are not to be updated
    # even when passed as argunments.
    skip_over_keys = ["id", "email", "created_at", "updated_at"]

    is_obj = storage.get(User, user_id)
    # The following check for exceptions that could arise.
    if is_obj is None:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")

    # Retrieve the passed in JSON args as a Python Dict.
    posted_data = request.get_json()
    for key, value in posted_data.items():
        if key in skip_over_keys:
            continue
        setattr(is_obj, key, value)
    # once attribute is update, calling the save()
    # since the update happend while that session was this open
    # calling the save() on that session will commit the change.
    storage.save()
    # A dict repr of the recent change is retrieved
    # for further json serialization
    dict_repr = User(**is_obj.__dict__).to_dict()
    json_repr = json.dumps(dict_repr, indent=2)
    return Response(f"{json_repr}\n",  mimetype='application/json', status=200)
