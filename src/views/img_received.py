from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class ImgReceivedView:
    '''
        Responsável por interagir com HTTP
    '''
    
    def validate_image(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        img = body["img"]
        print(img)
        #Lógica de regra de negócio
        print("Estou na view")

        # retorno http
        return HttpResponse(status_code=200, body={ "hello": "world" })
    