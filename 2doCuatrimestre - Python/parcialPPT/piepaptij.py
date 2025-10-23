import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
import random

class JuegoPiedraPapelTijera:
    def __init__(self):
        # Configuración de la ventana principal
        self.root = tk.Tk()
        self.root.title("Piedra, Papel, Tijera")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)
        
        # Variables del juego
        self.contadorUsuario = 0
        self.contadorMaquina = 0
        self.contadorEmpates = 0
        self.opciones = {1: "piedra", 2: "papel", 3: "tijera"}
        
        # Crear la interfaz
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Título principal
        titulo = tk.Label(
            self.root, 
            text="✊🏾Piedra, ✋🏾Papel, ✌🏾Tijera", 
            font=("Arial", 24, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        titulo.pack(pady=20)
        
        # Frame para el marcador
        marcador_frame = tk.Frame(self.root, bg='#f0f0f0')
        marcador_frame.pack(pady=10)
        
        # Marcador
        self.marcador_label = tk.Label(
            marcador_frame,
            text=f"Usuario: {self.contadorUsuario}  |  Máquina: {self.contadorMaquina}  |  Empates: {self.contadorEmpates}",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0',
            fg='#34495e'
        )
        self.marcador_label.pack()
        
        # Frame para mostrar las elecciones
        elecciones_frame = tk.Frame(self.root, bg='#f0f0f0')
        elecciones_frame.pack(pady=20)
        
        # Labels para mostrar las elecciones
        tk.Label(elecciones_frame, text="Tu elección:", font=("Arial", 12, "bold"), bg='#f0f0f0').pack()
        self.usuario_label = tk.Label(
            elecciones_frame, 
            text="", 
            font=("Arial", 14),
            bg='#e8f4fd',
            fg='#2980b9',
            width=15,
            relief='raised',
            bd=2
        )
        self.usuario_label.pack(pady=5)
        
        tk.Label(elecciones_frame, text="Elección de la máquina:", font=("Arial", 12, "bold"), bg='#f0f0f0').pack()
        self.maquina_label = tk.Label(
            elecciones_frame, 
            text="", 
            font=("Arial", 14),
            bg='#fdeaea',
            fg='#e74c3c',
            width=15,
            relief='raised',
            bd=2
        )
        self.maquina_label.pack(pady=5)
        
        # Frame para el resultado
        resultado_frame = tk.Frame(self.root, bg='#f0f0f0')
        resultado_frame.pack(pady=10)
        
        self.resultado_label = tk.Label(
            resultado_frame,
            text="",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0',
            fg='#27ae60'
        )
        self.resultado_label.pack()
        
        # Frame para los botones
        botones_frame = tk.Frame(self.root, bg='#f0f0f0')
        botones_frame.pack(pady=30)
        
        # Botones de elección
        self.boton_piedra = tk.Button(
            botones_frame,
            text="Piedra",
            font=("Arial", 14, "bold"),
            bg='#95a5a6',
            fg='white',
            width=12,
            height=2,
            command=lambda: self.jugar("piedra"),
            relief='raised',
            bd=3
        )
        self.boton_piedra.pack(side=tk.LEFT, padx=10)
        
        self.boton_papel = tk.Button(
            botones_frame,
            text="Papel",
            font=("Arial", 14, "bold"),
            bg='#3498db',
            fg='white',
            width=12,
            height=2,
            command=lambda: self.jugar("papel"),
            relief='raised',
            bd=3
        )
        self.boton_papel.pack(side=tk.LEFT, padx=10)
        
        self.boton_tijera = tk.Button(
            botones_frame,
            text="Tijera",
            font=("Arial", 14, "bold"),
            bg='#e74c3c',
            fg='white',
            width=12,
            height=2,
            command=lambda: self.jugar("tijera"),
            relief='raised',
            bd=3
        )
        self.boton_tijera.pack(side=tk.LEFT, padx=10)
        
        # Botón de reinicio
        self.boton_reinicio = tk.Button(
            self.root,
            text="Reiniciar Juego",
            font=("Arial", 12, "bold"),
            bg='#f39c12',
            fg='white',
            width=15,
            height=2,
            command=self.reiniciar_juego,
            relief='raised',
            bd=3
        )
        self.boton_reinicio.pack(pady=20)
        
    def jugar(self, eleccion_usuario):
        # Generar elección aleatoria de la máquina
        eleccion_maquina_num = random.randint(1, 3)
        eleccion_maquina = self.opciones[eleccion_maquina_num]
        
        # Mostrar las elecciones
        self.usuario_label.config(text=f"Tu: {eleccion_usuario.title()}")
        self.maquina_label.config(text=f"PC: {eleccion_maquina.title()}")
        
        # Determinar el resultado
        if eleccion_usuario == eleccion_maquina:
            self.contadorEmpates += 1
            resultado = "¡Empate!"
            color = '#f39c12'
        elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or \
             (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or \
             (eleccion_usuario == "tijera" and eleccion_maquina == "papel"):
            self.contadorUsuario += 1
            resultado = "¡Ganaste esta ronda!"
            color = '#27ae60'
        else:
            self.contadorMaquina += 1
            resultado = "Perdiste esta ronda"
            color = '#e74c3c'
        
        # Mostrar resultado
        self.resultado_label.config(text=resultado, fg=color)
        
        # Actualizar marcador
        self.marcador_label.config(
            text=f"Usuario: {self.contadorUsuario}  |  Máquina: {self.contadorMaquina}  |  Empates: {self.contadorEmpates}"
        )
        
        # Verificar si alguien llegó a 3 puntos
        if self.contadorUsuario >= 3 or self.contadorMaquina >= 3:
            self.finalizar_juego()
    
    def finalizar_juego(self):
        # Deshabilitar botones
        self.boton_piedra.config(state='disabled')
        self.boton_papel.config(state='disabled')
        self.boton_tijera.config(state='disabled')
        
        # Mostrar resultado final
        if self.contadorUsuario >= 3:
            mensaje = f"¡FELICIDADES! ¡GANASTE EL JUEGO!\n\nMarcador final:\nUsuario: {self.contadorUsuario}\nMáquina: {self.contadorMaquina}\nEmpates: {self.contadorEmpates}"
            messagebox.showinfo("¡Ganaste!", mensaje)
        else:
            mensaje = f"¡La máquina ganó el juego!\n\nMarcador final:\nMáquina: {self.contadorMaquina}\nUsuario: {self.contadorUsuario}\nEmpates: {self.contadorEmpates}"
            messagebox.showinfo("¡Perdiste!", mensaje)
        
        self.resultado_label.config(
            text="¡Juego terminado! Presiona 'Reiniciar' para jugar de nuevo",
            fg='#8e44ad'
        )
    
    def reiniciar_juego(self):
        # Reiniciar contadores
        self.contadorUsuario = 0
        self.contadorMaquina = 0
        self.contadorEmpates = 0
        
        # Limpiar labels
        self.usuario_label.config(text="")
        self.maquina_label.config(text="")
        self.resultado_label.config(text="")
        
        # Actualizar marcador
        self.marcador_label.config(
            text=f"Usuario: {self.contadorUsuario}  |  Máquina: {self.contadorMaquina}  |  Empates: {self.contadorEmpates}"
        )
        
        # Habilitar botones
        self.boton_piedra.config(state='normal')
        self.boton_papel.config(state='normal')
        self.boton_tijera.config(state='normal')
    
    def ejecutar(self):
        self.root.mainloop()

# Crear y ejecutar el juego
if __name__ == "__main__":
    juego = JuegoPiedraPapelTijera()
    juego.ejecutar() 
