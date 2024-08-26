from typing import Dict
from io import BytesIO
import logging
from PIL import Image
import dill 
from fastai.vision.learner import load_learner
from src.drivers.img_handler import ImgHandler
from src.drivers.img_classification import img_classification

class ImgReceivedController:
	'''
		Responsável por implementar a regra de negócio
	'''
	def __init__(self):
		self.__learn = None
		self.__model = "model_soy_v4.pkl"
 
	def predict_image(self, img_base64) -> Dict:
		img_decoder = ImgHandler()
		logging.basicConfig(level=logging.INFO)
  
		#carrega o modelo
		self.__load_model()
  
		try:
			#decodifica a imagem
			img_bytes = img_decoder.decodifica_img(img_base64)
		
			#transforma a imagem em um objeto PIL
			img = Image.open(BytesIO(img_bytes))
			print("Imagem decodificada com sucesso:", img)
   
			classification = img_classification(img)

			if classification:
				
				resize_img = img.resize((460, 460))
				#realiza a predição
				pred_class, pred_idx, pred_outputs = self.__learn.predict(resize_img)
				logging.info("Predição realizada com sucesso: %s, %s, %s", pred_class, pred_idx, pred_outputs)

				classes = self.__learn.dls.vocab
				class_probs = {cls: prob for cls, prob in zip(classes, pred_outputs)}

				return self.__format_response(pred_class, class_probs)
			return {"message": "Soja não identificada"}
		except Exception as e:
			print(f"Erro ao realizar a predição: {e}")
			return {
				"error": {
					"message": "Erro ao realizar a predição"
				}
			}
	
	def __load_model(self):
		self.__learn = load_learner(self.__model, pickle_module=dill)
 	
	def __format_response(self, pred_class, prediction_probs) -> Dict:
		return {
			"pred_class": str(pred_class),
			"lagarta_das_vagens_prob": float(prediction_probs.get("Lagarta_das_vagens")),
			"lagarta_soja_prob": float(prediction_probs.get("Lagarta_soja")),
			"percevejo_soja_prob": float(prediction_probs.get("Percevejo_soja")),
			"healthy_prob": float(prediction_probs.get("Saudavel")),
			"vaquinha_prob": float(prediction_probs.get("Vaquinha_verde_amarelo"))
		}
