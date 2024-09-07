from flask import Blueprint

# Define the Blueprint
evaluations = Blueprint('evaluations', __name__)

from . import routes #check syntex here
