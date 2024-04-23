from flask import Flask
from flask_cors import CORS
from src.main.routes.model_routes import model_routes_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(model_routes_bp)
