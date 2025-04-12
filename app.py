from flask import Flask
from config import db, migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuración JWT
app.config['JWT_SECRET_KEY'] = "hola"
jwt = JWTManager(app)

# Configuración Base de Datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar DB y migraciones
db.init_app(app)
migrate.init_app(app, db)

# Configurar Swagger
app.config['SWAGGER'] = {
    'title': 'User API',
    'uiversion': 3
}
Swagger(app)

# Rutas
from Routes.user import user_bp
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
