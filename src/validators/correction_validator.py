from cerberus import Validator

def correction_result_received_validator(request: any) -> None:
    body_validator = Validator({    
        "data": {
            "type": "dict",
            "required": True,
            "schema": {
                "image": {
                    "type": "dict",
                    "required": True,
                    "schema": {
                        "base64": {"type": "string", "required": True, "empty": False}
                }
            },
            "result": {"type": "string", "required": True},
            "result_correction": {"type": "string", "required": True}
        }
    }
    }) 
    
    response = body_validator.validate(request.json)
    if response is False:
        raise Exception(body_validator.errors)
    