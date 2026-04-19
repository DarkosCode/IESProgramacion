import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
from hand_recognizer import HandRecognizer
from game_logic import RockPaperScissorsGame

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Inicializar lógica del juego y reconocedor
        self.game = RockPaperScissorsGame()
        try:
            # Asegúrate que los archivos del modelo estén en la misma carpeta
            self.recognizer = HandRecognizer("keras_model.h5", "labels.txt")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo inicializar el modelo: {e}")
            self.window.destroy()
            return

        # UI Components
        # Frame para el video
        self.video_frame = tk.Label(window)
        self.video_frame.pack(padx=10, pady=10)

        # Etiqueta de información (Resultado)
        self.info_label = tk.Label(window, text="Presiona 'JUGAR' para capturar tu gesto", font=("Helvetica", 16))
        self.info_label.pack(pady=5)

        # Etiqueta de Puntaje
        self.score_label = tk.Label(window, text="Puntajes - Usuario: 0 | CPU: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=5)

        # Botón Jugar
        self.play_button = tk.Button(window, text="JUGAR", font=("Helvetica", 20, "bold"), command=self.play_round, bg="#4CAF50", fg="white")
        self.play_button.pack(pady=20, ipadx=10, ipady=5)
        
        # Bucle de actualización de video
        self.update_video()

        # Manejar cierre de ventana
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_video(self):
        frame = self.recognizer.get_frame()
        if frame is not None:
            # Convertir de BGR (OpenCV) a RGB (Pillow)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_frame.imgtk = imgtk
            self.video_frame.configure(image=imgtk)
        
        # Actualizar cada 10ms
        self.window.after(10, self.update_video)

    def play_round(self):
        # 1. Obtener frame actual y predecir
        frame = self.recognizer.get_frame()
        if frame is None:
            return

        gesture, confidence = self.recognizer.predict_gesture(frame)
        
        # Puedes ajustar este umbral de confianza si es necesario
        if confidence < 0.7:
             self.info_label.config(text=f"No estoy seguro ({int(confidence*100)}%)... intenta de nuevo.", fg="orange")
             return

        # 2. Jugar
        cpu_choice = self.game.get_cpu_choice()
        result = self.game.determine_winner(gesture, cpu_choice)
        
        # 3. Actualizar UI
        user_score, cpu_score = self.game.get_scores()
        self.score_label.config(text=f"Puntajes - Usuario: {user_score} | CPU: {cpu_score}")
        
        result_text = f"Tú: {gesture} vs CPU: {cpu_choice}\n"
        if result == "Usuario":
            result_text += "¡GANASTE!"
            color = "green"
        elif result == "CPU":
            result_text += "Perdiste..."
            color = "red"
        else:
            result_text += "Empate"
            color = "blue"
            
        self.info_label.config(text=result_text, fg=color)

    def on_closing(self):
        if hasattr(self, 'recognizer'):
            self.recognizer.release()
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root, "Piedra, Papel, Tijera AI")
    root.mainloop()
