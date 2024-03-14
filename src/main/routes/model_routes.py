from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.img_received import ImgReceivedView

model_routes_bp = Blueprint('model_routes', __name__)

@model_routes_bp.route('/predict', methods=["POST"])
def predict():
    img_received_view = ImgReceivedView()
    http_request = HttpRequest(body=request.json)
    
    response = img_received_view.validate_image(http_request)
    
    return jsonify(response.body), response.status_code
