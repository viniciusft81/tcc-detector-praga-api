from flask import Blueprint, request, jsonify

model_routes_bp = Blueprint('model_routes', __name__)

@model_routes_bp.route('/predict', methods=["POST"])
def predict():
    print(request.json)
    return jsonify({ "resp": "ok" }), 200
