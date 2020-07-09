import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

longitud, altura = 100, 100
modelo = "/content/drive/My Drive/I^2GPF/ModeloEntrenado/modeloV2.h5"
pesos = "/content/drive/My Drive/I^2GPF/ModeloEntrenado/pesosV2.h5"

cnn = load_model(modelo)
cnn.load_weights(pesos)

def predict(file):
    x = load_img(file, target_size=(longitud,altura))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    arreglo = cnn.predict(x) ##[[1,0]]
    resultado = arreglo[0]
    respuesta = np.argmax(resultado)  

    if (respuesta == 0):
        print ("Con barbijo")
    elif (respuesta == 1):
        print ("Sin barbijo")
  
predict("/content/drive/My Drive/I^2GPF/Pruebas/yosin.jpg")