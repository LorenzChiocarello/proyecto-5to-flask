import mysql.connector
from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host="localhost",
    user="root",
    password="123456789",
    database="Escuela"
)

def get_db():
    return pool.get_connection()
