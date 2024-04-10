from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.img_received_controller import ImgReceivedController

class ImgReceivedView:
    '''
        Responsável por interagir com HTTP
    '''
    
    def validate_image(self, http_request: HttpRequest) -> HttpResponse:
        img_received_controller = ImgReceivedController()
        
        body = http_request.body
        img_base64 = body["inputs"][0]["data"]["image"]["base64"]
    
        #Lógica de regra de negócio
        formatted_response = img_received_controller.predict_image(img_base64)

        # retorno http
        return HttpResponse(status_code=200, body=formatted_response)
    