from flask import Blueprint
from controllers.curso_controller import get_all_cursos

curso_bp = Blueprint("curso_bp", __name__)

curso_bp.route("/", methods=["GET"])(get_all_cursos)
