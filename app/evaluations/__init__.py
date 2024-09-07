from flask import Blueprint

evaluations_bp = Blueprint('evaluations', __name__)

from . import routes #check syntex here
