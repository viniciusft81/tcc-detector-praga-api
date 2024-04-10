#from PIL import Image
#from io import BytesIO
#from fastai.vision.all import *
import base64

class ImgHandler():
    # def __init__(self) -> None:
    #     self.__learn = None
    #     self.__model_path = './model_soy.pkl'
     
    # def __load_model(self):
    #     self.__learn = load_learner(self.__model_path, dill)
        
    def decodifica_img(self, image_base64):
        #carrega o modelo
        #self.__load_model()
        
        #decodifica a imagem
        img_decoded = base64.b64decode(image_base64)
        
        #transforma a imagem em um objeto PIL
        #img = Image.open(BytesIO(img_decoded))
        
        #realiza a predição
        #pred_class, pred_idx, outputs = self.__learn.predict(img)
        
        return img_decoded
    