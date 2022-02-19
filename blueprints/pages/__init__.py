from flask import Blueprint
from .main_page import main_page_blueprint

pages_blueprint = Blueprint("pages_blueprint", __name__)
pages_blueprint.register_blueprint(main_page_blueprint)
