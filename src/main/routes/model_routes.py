from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.img_received_view import ImgReceivedView
from src.errors.error_handler import handle_errors

model_routes_bp = Blueprint('model_routes', __name__)

@model_routes_bp.route('/predict', methods=["POST"])
def predict():
    response = None
    try:
        img_received_view = ImgReceivedView()
    
        http_request = HttpRequest(body=request.json)
        response = img_received_view.validate_image(http_request)
    
    except Exception as e:
        response = handle_errors(e)
    
    return jsonify(response.body), response.status_code
