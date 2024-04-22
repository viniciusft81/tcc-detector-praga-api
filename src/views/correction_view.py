from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.correction_controller import CorrectionController

class CorrectionView:
    '''
        Responsável por interagir com HTTP
    '''
    
    def validate_correction(self, http_request: HttpRequest) -> HttpResponse:
        correction_controller = CorrectionController()
        
        body = http_request.body
        data_correction = body
    
        #Lógica de regra de negócio
        formatted_response = correction_controller.store_correction(data_correction)

        # retorno http
        return HttpResponse(status_code=200, body=formatted_response)