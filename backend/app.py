from flask import Flask
from flask_cors import CORS
from routes.curso_routes import curso_bp
from routes.estudiante_routes import estudiante_bp
from config.database import init_db

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3001"}}, supports_credentials=True)

init_db()

app.register_blueprint(curso_bp, url_prefix="/cursos")
app.register_blueprint(estudiante_bp, url_prefix="/estudiantes")

if __name__ == "__main__":
    app.run(debug=True)

