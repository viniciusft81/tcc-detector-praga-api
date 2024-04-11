from cerberus import Validator
import json

body = {
    "inputs": [
        {
            "data": {
                "image": {
                    "base64": "akfasmfkamfkanaksdamdamdaamdam"
                }
            }
        }
    ]
}

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

response = body_validator.validate(body)
json_response = json.dumps(body)

print(json_response)
print(response)
