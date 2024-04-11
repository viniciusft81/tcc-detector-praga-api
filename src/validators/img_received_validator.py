from cerberus import Validator

def image_received_validator(request: any) -> None:
    body_validator = Validator({    
        "inputs": {
            "type": "list",
            "required": True,
            "schema": {
                "type": "dict",
                "schema": {
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
                            }
                        }
                    }
                }
            }
        }
    }) 
    
    response = body_validator.validate(request.json)
    if response is False:
        raise Exception(body_validator.errors)
    