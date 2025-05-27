from flask import request, jsonify
from config.database import get_db

def get_all_estudiantes():
    conn = get_db()
    cursor = conn.cursor()
    query = """
        SELECT e.*, c.curso 
        FROM Estudiantes e 
        LEFT JOIN Cursos c ON e.idcurso = c.id
        ORDER BY c.curso ASC
    """
    cursor.execute(query)
    estudiantes = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(estudiantes)

def get_estudiante_by_id(id):
    conn = get_db()
    cursor = conn.cursor()
    query = "SELECT e.*, c.curso FROM Estudiantes e LEFT JOIN Cursos c ON e.idcurso = c.id WHERE e.id = ?"
    cursor.execute(query, (id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        return jsonify({"message": "Estudiante no encontrado"}), 404
    
    estudiante = dict(row)
    return jsonify(estudiante)

def create_estudiante():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    query = "INSERT INTO Estudiantes (nombre, apellido, fechanacimiento, idcurso) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (data["nombre"], data["apellido"], data["fechanacimiento"], data["idcurso"]))
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": student_id, **data}), 201

def update_estudiante(id):
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    query = "UPDATE Estudiantes SET nombre = ?, apellido = ?, fechanacimiento = ?, idcurso = ? WHERE id = ?"
    cursor.execute(query, (data["nombre"], data["apellido"], data["fechanacimiento"], data["idcurso"], id))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"message": "Estudiante no encontrado"}), 404
    
    conn.close()
    return jsonify({"message": "Estudiante actualizado exitosamente"})

def delete_estudiante(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Estudiantes WHERE id = ?", (id,))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"message": "Estudiante no encontrado"}), 404
    
    conn.close()
    return jsonify({"message": "Estudiante eliminado exitosamente"})
