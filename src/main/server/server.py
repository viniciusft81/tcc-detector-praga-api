from flask import Flask
from src.main.routes.model_routes import model_routes_bp

app = Flask(__name__)

app.register_blueprint(model_routes_bp)
