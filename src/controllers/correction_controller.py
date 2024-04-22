from typing import Dict
from pymongo import MongoClient
from src.drivers.env_db import connection_db

class CorrectionController:
    
    def __init__(self):
        self.__connection_string = connection_db
        
    def store_correction(self, data_correction: dict) -> Dict:
        try:
            print(self.__connection_string[0])
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
        