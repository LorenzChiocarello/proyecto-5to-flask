import sqlite3
import os

DB_NAME = "escuela.db"

def get_db():
    """Conecta a la base de datos SQLite"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn

def init_db():
    """Crea las tablas si no existen"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            curso TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            fechanacimiento DATE NOT NULL,
            idcurso INTEGER,
            FOREIGN KEY (idcurso) REFERENCES Cursos (id)
        )
    ''')
    
    cursor.execute('SELECT COUNT(*) FROM Cursos')
    if cursor.fetchone()[0] == 0:
        cursos_ejemplo = [
            ('1A',),
            ('2A',),
            ('3B',)
        ]
        cursor.executemany('INSERT INTO Cursos (curso) VALUES (?)', cursos_ejemplo)
        
        cursor.execute('''
            INSERT INTO Estudiantes (nombre, apellido, fechanacimiento, idcurso) 
            VALUES (?, ?, ?, ?)
        ''', ('Federico', 'Lopez', '2020-04-07', 2))
    
    conn.commit()
    conn.close()
