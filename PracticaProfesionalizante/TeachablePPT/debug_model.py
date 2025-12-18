import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

print("Versión de TensorFlow:", tf.__version__)
print("Versión de Numpy:", np.__version__)

try:
    print("Intentando cargar el modelo 'keras_model.h5'...")
    model = load_model("keras_model.h5", compile=False)
    print("¡Modelo cargado exitosamente!")
    model.summary()
except Exception as e:
    print("\n--- ERROR FATAL AL CARGAR EL MODELO ---")
    print(e)
    print("---------------------------------------")
