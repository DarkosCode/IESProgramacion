import cv2
import numpy as np
import tensorflow.keras
import random
import time
import os
import sys

# --- CONFIGURACIÓN PARA PORTABILIDAD ---
# Obtenemos la ruta absoluta de DONDE está este script ejecutándose
# Esto permite que funcione en tu PC y en tu Notebook sin cambiar código.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(SCRIPT_DIR, 'keras_model.h5')
LABELS_PATH = os.path.join(SCRIPT_DIR, 'labels.txt')

# Verificar que los archivos existan antes de arrancar
if not os.path.exists(MODEL_PATH) or not os.path.exists(LABELS_PATH):
    print("ERROR CRÍTICO: No se encuentran los archivos del modelo.")
    print(f"Buscando en: {SCRIPT_DIR}")
    print("Asegúrate de que 'keras_model.h5' y 'labels.txt' están en la misma carpeta que este script.")
    sys.exit()

# --- CARGA DEL MODELO ---
print("Cargando modelo... por favor espera.")
# Desactivamos la notación científica para claridad
np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model(MODEL_PATH, compile=False)
class_names = open(LABELS_PATH, 'r').readlines()

# --- CONFIGURACIÓN DE CÁMARA ---
# Intentamos abrir la cámara por defecto (0)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo abrir la cámara. Intenta cambiar el índice a 1 o verifica los permisos.")
    sys.exit()

# Opciones para la computadora
OPCIONES = ["Piedra", "Papel", "Tijera"]

def obtener_jugada_usuario(prediction_array):
    """Devuelve el nombre de la clase con mayor confianza"""
    max_index = np.argmax(prediction_array)
    # Limpiamos el texto (ej: "0 Piedra\n" -> "Piedra")
    label = class_names[max_index].strip().split(' ', 1)[1]
    confidence = prediction_array[0][max_index]
    return label, confidence

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "EMPATE"
    elif (jugador == "Piedra" and computadora == "Tijera") or \
         (jugador == "Papel" and computadora == "Piedra") or \
         (jugador == "Tijera" and computadora == "Papel"):
        return "¡GANASTE! :D"
    else:
        return "PERDISTE :("

print("¡Sistema listo!")
print("Presiona 'ESPACIO' para jugar una ronda.")
print("Presiona 'Q' para salir.")

# Variables de estado del juego
mensaje_resultado = ""
mensaje_computadora = ""
timer_inicio = 0
jugando = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Espejamos la cámara para que sea más natural
    frame = cv2.flip(frame, 1)
    
    # Copia del frame para mostrar en pantalla
    display_frame = frame.copy()

    # --- LÓGICA DEL JUEGO ---
    if jugando:
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - timer_inicio
        
        if tiempo_transcurrido < 3:
            # Cuenta regresiva: 3, 2, 1...
            countdown = 3 - int(tiempo_transcurrido)
            cv2.putText(display_frame, str(countdown), (280, 240), cv2.FONT_HERSHEY_BOLD, 7, (0, 255, 255), 10)
        else:
            # ¡MOMENTO DE LA VERDAD! Capturamos y predecimos
            
            # 1. Preparar imagen para el modelo (224x224)
            resized = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
            image_array = np.asarray(resized, dtype=np.float32).reshape(1, 224, 224, 3)
            image_array = (image_array / 127.0) - 1 # Normalizar
            
            # 2. Predecir
            prediction = model.predict(image_array, verbose=0)
            jugada_usuario, confianza = obtener_jugada_usuario(prediction)
            
            # 3. Jugada de la PC
            jugada_pc = random.choice(OPCIONES)
            
            # 4. Resultado
            resultado = determinar_ganador(jugada_usuario, jugada_pc)
            
            # Guardamos los mensajes para mostrarlos
            mensaje_resultado = f"Tu: {jugada_usuario} vs PC: {jugada_pc} -> {resultado}"
            print(mensaje_resultado) # También lo imprimimos en terminal
            
            jugando = False # Terminamos la ronda
            
    # --- INTERFAZ GRÁFICA ---
    # Mostrar instrucciones
    cv2.putText(display_frame, "ESPACIO para jugar | Q para salir", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # Mostrar último resultado
    if mensaje_resultado:
        color = (0, 255, 0) if "GANASTE" in mensaje_resultado else (0, 0, 255)
        if "EMPATE" in mensaje_resultado: color = (255, 255, 0)
        
        # Ajustar tamaño de texto para que quepa
        cv2.putText(display_frame, mensaje_resultado, (10, 450), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow('Piedra, Papel o Tijera - IA', display_frame)

    # Captura de teclas
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord(' ') and not jugando:
        jugando = True
        timer_inicio = time.time()
        mensaje_resultado = "Preparate..."

cap.release()
cv2.destroyAllWindows()