from flask import Blueprint
from controllers.estudiante_controller import get_all_estudiantes, get_estudiante_by_id, create_estudiante, update_estudiante, delete_estudiante

estudiante_bp = Blueprint("estudiante_bp", __name__)

estudiante_bp.route("/", methods=["GET"])(get_all_estudiantes)
estudiante_bp.route("/<int:id>", methods=["GET"])(get_estudiante_by_id)
estudiante_bp.route("/", methods=["POST"])(create_estudiante)
estudiante_bp.route("/<int:id>", methods=["PUT"])(update_estudiante)
estudiante_bp.route("/<int:id>", methods=["DELETE"])(delete_estudiante)
