from typing import Dict
from pymongo import MongoClient

class CorrectionController:
    
    def __init__(self):
        self.__connection_string = "mongodb+srv://viniciusft81:xhkLIRmcOQs6chPa@detector-praga-db.rkg0l9g.mongodb.net/"
        
    def store_correction(self, data_correction: dict) -> Dict:
        try:
            client = MongoClient(self.__connection_string)
            db = client["detector-praga-db"]
            collection = db["corrections"]
            collection.insert_one(data_correction)
            
            return self.__format_response()
        except Exception as e:
            print("Erro ao armazenar a correção", e)
            return {
                "message": "Erro ao armazenar a correção"
            }
    
    def __format_response(self) -> Dict:
        return {
            "message": "Correção armazenada com sucesso"
        }