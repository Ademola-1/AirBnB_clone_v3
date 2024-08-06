from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")
"""The blueprint for the AIrBnB clone API"""

from api.v1.views.index import *
from api.v1.views.amenities import *
from models.base_model import *
from api.v1.views.states import *
