from typing import Dict
from io import BytesIO
from PIL import Image
import dill
from fastai.vision.learner import load_learner
from src.drivers.img_handler import ImgHandler

class ImgReceivedController:
	'''
		Responsável por implementar a regra de negócio
	'''
	def __init__(self):
		self.__learn = None
 
	def predict_image(self, img_base64) -> Dict:
		img_decoder = ImgHandler()
  
		#carrega o modelo
		self.__load_model()
  
		try:
			#decodifica a imagem
			img_bytes = img_decoder.decodifica_img(img_base64)
		
			#transforma a imagem em um objeto PIL
			img = Image.open(BytesIO(img_bytes))
			print("Imagem decodificada com sucesso:", img)

			resize_img = img.resize((460, 460))
			#show_image(img)
			#realiza a predição
			pred_class, pred_idx, pred_outputs = self.__learn.predict(resize_img)
			print("Predição realizada com sucesso:", pred_class, pred_idx, pred_outputs)
		
			return self.__format_response(pred_class, pred_outputs)
		except Exception as e:
			print(f"Erro ao realizar a predição: {e}")
			return {
				"error": {
					"message": "Erro ao realizar a predição"
				}
			}
	
	def __load_model(self):
		self.__learn = load_learner("model_soy.pkl", pickle_module=dill)
 	
	def __format_response(self, prediction_class, percentage) -> Dict:
		return [{
			"data": {
				"pred_class": str(prediction_class),
				"pred_prob": [float(prob) for prob in percentage]
			}
		}]
