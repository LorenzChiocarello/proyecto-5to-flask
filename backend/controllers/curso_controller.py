from flask import jsonify
from config.database import get_db

def get_all_cursos():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Cursos")
    cursos = cursor.fetchall()
    db.close()
    return jsonify(cursos)
