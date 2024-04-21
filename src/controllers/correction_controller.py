from typing import Dict
from pymongo import MongoClient

class CorrectionController:
    
    def __init__(self):
        self.__connection_string = "mongodb://localhost:27017/"
    
    def store_correction(self, data_correction: dict) -> Dict:
        try:
            client = MongoClient(self.__connection_string)
            db = client["detector-praga-db"]
            collection = db["corrections"]
            collection.insert_one(data_correction)
            return self.__format_response()
        except Exception as e:
            return {
                "message": "Erro ao armazenar a correção", "error": f"{e}"
            }
    
    def __format_response(self) -> Dict:
        return {
            "message": "Correção armazenada com sucesso"
        }