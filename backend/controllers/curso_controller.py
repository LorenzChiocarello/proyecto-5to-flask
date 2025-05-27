from flask import jsonify
from config.database import get_db

def get_all_cursos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cursos")
    cursos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(cursos)

