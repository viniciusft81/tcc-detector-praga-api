from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.img_received_view import ImgReceivedView
from src.views.correction_view import CorrectionView
from src.errors.error_handler import handle_errors
from src.validators.img_received_validator import image_received_validator
from src.validators.correction_validator import correction_result_received_validator

model_routes_bp = Blueprint('model_routes', __name__)

@model_routes_bp.route('/predict', methods=["POST"])
def predict():
    response = None
    try:
        image_received_validator(request)
        img_received_view = ImgReceivedView()
    
        http_request = HttpRequest(body=request.json)
        response = img_received_view.validate_image(http_request)
    
    except Exception as e:
        response = handle_errors(e)
    
    return jsonify(response.body), response.status_code

@model_routes_bp.route('/result_correction', methods=["POST"])
def result_correction():
    response = None
    try:
        correction_result_received_validator(request)
        correction_view =  CorrectionView()
    
        http_request = HttpRequest(body=request.json)
        response = correction_view.validate_correction(http_request)
    
    except Exception as e:
        response = handle_errors(e)
    
    return jsonify(response.body), response.status_code