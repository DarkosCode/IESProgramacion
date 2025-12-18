import cv2
import numpy as np
import os

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

try:
    from tf_keras.models import load_model
    print("Using tf_keras (legacy compatibility)")
except ImportError:
    from tensorflow.keras.models import load_model
    print("Using tensorflow.keras (standard)")

class HandRecognizer:
    def __init__(self, model_path, labels_path):
        """
        Inicializa el reconocedor de manos.
        :param model_path: Ruta al archivo del modelo .h5
        :param labels_path: Ruta al archivo de etiquetas .txt
        """
        # Deshabilitar notación científica para claridad
        np.set_printoptions(suppress=True)
        
        # Cargar el modelo
        try:
            self.model = load_model(model_path, compile=False)
        except Exception as e:
            raise RuntimeError(f"Error al cargar el modelo: {e}")

        # Cargar las etiquetas
        try:
            with open(labels_path, "r") as f:
                self.class_names = [line.strip() for line in f.readlines()]
        except Exception as e:
            raise RuntimeError(f"Error al cargar las etiquetas: {e}")

        # Inicializar la cámara
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Advertencia: No se pudo acceder a la cámara web.")

    def get_frame(self):
        """
        Captura un frame de la cámara.
        :return: El frame capturado o None si falla.
        """
        if not self.cap.isOpened():
            return None
            
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def predict_gesture(self, frame):
        """
        Predice el gesto en el frame dado.
        :param frame: Imagen capturada por la cámara.
        :return: (Nombre de la clase, Puntaje de confianza)
        """
        if frame is None:
            return None, 0.0

        # Redimensionar la imagen a 224x224 (entrada requerida por Teachable Machine)
        image = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

        # Convertir la imagen a un array de numpy y normalizar
        # La imagen se normaliza de [0, 255] a [-1, 1]
        image_array = np.asarray(image, dtype=np.float32)
        normalized_image_array = (image_array / 127.5) - 1

        # Crear el batch de datos (1 imagen)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array

        # Predecir
        prediction = self.model.predict(data)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]

        # Limpiar el nombre de la clase (quita el índice inicial '0 ', '1 ', etc.)
        # Ejemplo: '0 Piedra' -> 'Piedra'
        clean_class_name = class_name[2:].strip()

        return clean_class_name, confidence_score

    def release(self):
        """Libera los recursos de la cámara."""
        if self.cap.isOpened():
            self.cap.release()
