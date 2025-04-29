from flask import request, jsonify
from config.database import get_db

def get_all_estudiantes():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = """
        SELECT e.*, c.curso 
        FROM Estudiantes e 
        LEFT JOIN Cursos c ON e.idcurso = c.id
        ORDER BY c.curso ASC
    """
    cursor.execute(query)
    estudiantes = cursor.fetchall()
    db.close()
    return jsonify(estudiantes)

def get_estudiante_by_id(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT e.*, c.curso FROM Estudiantes e LEFT JOIN Cursos c ON e.idcurso = c.id WHERE e.id = %s"
    cursor.execute(query, (id,))
    estudiante = cursor.fetchone()
    db.close()
    if not estudiante:
        return jsonify({"message": "Estudiante no encontrado"}), 404
    return jsonify(estudiante)

def create_estudiante():
    data = request.json
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO Estudiantes (nombre, apellido, fechanacimiento, idcurso) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (data["nombre"], data["apellido"], data["fechanacimiento"], data["idcurso"]))
    db.commit()
    student_id = cursor.lastrowid
    db.close()
    return jsonify({"id": student_id, **data}), 201

def update_estudiante(id):
    data = request.json
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE Estudiantes SET nombre = %s, apellido = %s, fechanacimiento = %s, idcurso = %s WHERE id = %s"
    cursor.execute(query, (data["nombre"], data["apellido"], data["fechanacimiento"], data["idcurso"], id))
    db.commit()
    if cursor.rowcount == 0:
        db.close()
        return jsonify({"message": "Estudiante no encontrado"}), 404
    db.close()
    return jsonify({"message": "Estudiante actualizado exitosamente"})

def delete_estudiante(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Estudiantes WHERE id = %s", (id,))
    db.commit()
    if cursor.rowcount == 0:
        db.close()
        return jsonify({"message": "Estudiante no encontrado"}), 404
    db.close()
    return jsonify({"message": "Estudiante eliminado exitosamente"})
