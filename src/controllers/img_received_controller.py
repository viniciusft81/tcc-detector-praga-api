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
   
				prob_prague, prob_healthy = float(pred_outputs[0]), float(pred_outputs[1])
				logging.info("probs=> %s, %s", prob_prague, prob_healthy)
		
				return self.__format_response(pred_class, prob_prague, prob_healthy)
			else:
				return {
					"message": "Planta não identificada"
				}
		except Exception as e:
			print(f"Erro ao realizar a predição: {e}")
			return {
				"error": {
					"message": "Erro ao realizar a predição"
				}
			}
	
	def __load_model(self):
		self.__learn = load_learner("model_soy.pkl", pickle_module=dill)
 	
	def __format_response(self, prediction_class, prediction_prob_prague, prediction_prob_healthy) -> Dict:
		return {
			"pred_class": str(prediction_class),
			"prague_prob": prediction_prob_prague, 
    		"healthy_prob": prediction_prob_healthy
		}
