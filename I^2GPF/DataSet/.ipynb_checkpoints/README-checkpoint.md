# Dataset
Ambos dataset tienen la misma estructura. Dos directorios: "Entrenamiento" y "Validacion", a su vez ambos directorios estan comuestos por otros dos directorios: "ConBarbijo" y "SinBarbijo". Como su nombre lo indica, el primer directorio "Entrenamiento" sirve para entrenar la red, mientras que el segundo "Validacion" sirve para hacer las validaciones despues de cada iteracion. 

La imagenes se obtuvieron de dos lugares:
* De un dataset previo desarrollado por "prajnasb". Quien usando imagenes de personas sin barbijo, con edicion añadio un barbijo a su rostro. De dicho dataset tome aproximadamente 400 imagenes. Si bien el dataset contaba con muchas mas imagenes, solo tome aquellas que no habian sido modificadas para aumentar el dataset (por ejemplo iamgenes que estaban rotadas o desplazadas). Ejemplo de la edicion:
![1-with-mask.jpg]