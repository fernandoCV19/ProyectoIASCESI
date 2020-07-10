# Proyecto IA SCESI
## Nombre del proyecto
Identificador inteligente de gente con proteccion facial (I^2GPF)
## Descripcion 
Dada una imagen que contanga un rostro de entrada, la red neuronal sera capaz de identificar si la persona esta usando o no un barbijo.
## Tecnologias a usar 
* Python 
* TensorFlow
* Keras
* Google Colab
* Google Drive
* OpenCV 
* Haarcascade

## IMPORTANTE 
Este repositorio contiene el proceso de creacion del proyeto, asi como varios intentos de redes neorunales, ademas del dataset utilizado en el entrenamiento de la red, los cuales incrementan en gran medida el tamaño del repositorio, Si solo deseas probar el modelo, ingresa al siguiente link: https://github.com/fernandoCV19/ProyectoIASCESI-LightVersion.git 
El cual contiene:
* El modelo de red neuronal que podujo mejores resultados a la hora de distinguir entre personas con barbijo y sin barbijo.
* Solo los archivos de haarcascade necesarios para el funcionamiento con una camara en vivo para la clasificacion de personas con barbijo y sin barbijo.
* Un programa que usa el reconocedor facial de haarcascade para clasificar los rostros.
* Un programa que usa el detector de ojos de haarcascade para encontrar la posicion de un rostro(el por que de este codigo se explica en su porpio directorio).
* Ambos programas cuentan con una version en un libro de jupyter lab y un ejecutable en python.
* Codigo para realizar una clasificacion unicamente con fotos utilizando el modelo entrenado.
