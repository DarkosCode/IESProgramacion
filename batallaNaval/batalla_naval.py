import tkinter as tk
from tkinter import messagebox
import random

# -----------------------------------------------------------------------------
# LÓGICA DEL JUEGO (BACKEND)
# -----------------------------------------------------------------------------

class Barco:
    """
    Representa un barco individual en el juego.
    Conoce su tamaño y cuántos golpes ha recibido.
    """
    def __init__(self, tamano):
        self.tamano = tamano
        self.golpes = 0

    def recibir_golpe(self):
        """Incrementa el contador de golpes del barco."""
        self.golpes += 1

    def esta_hundido(self):
        """Devuelve True si el número de golpes iguala al tamaño del barco."""
        return self.golpes >= self.tamano

class JuegoBatallaNaval:
    """
    Clase principal de la lógica del juego.
    Maneja el tablero, la colocación de barcos y la lógica de disparos.
    """
    def __init__(self):
        # Tablero 10x10 inicializado con None (vacío)
        # Se usará None para agua no descubierta, y objetos Barco para casillas con barco
        self.filas = 10
        self.columnas = 10
        self.tablero = []
        for i in range(self.filas):
            fila_nueva = []
            for j in range(self.columnas):
                fila_nueva.append(None)
            self.tablero.append(fila_nueva)
        
        # Matriz para rastrear disparos realizados (evita lógica duplicada en UI)
        # Valores posibles: None (sin disparo), "AGUA", "TOCADO", "HUNDIDO"
        self.disparos = []
        for i in range(self.filas):
            fila_disparos = []
            for j in range(self.columnas):
                fila_disparos.append(None)
            self.disparos.append(fila_disparos)
        
        self.flota = []
        # lista de los barcos a colocar/colocados, util para saber cuadno se hundieron todos
        self.colocar_barcos_aleatorios()

    def colocar_barcos_aleatorios(self):
        """
        Coloca la flota de barcos en posiciones aleatorias horizontales.
        Flota: 4 de tamaño 1, 3 de tamaño 2, 2 de tamaño 3.
        """
        barcos_a_colocar = [1]*4 + [2]*3 + [3]*2
        
        for tamano in barcos_a_colocar:
            colocado = False
            while not colocado:
                # Elegir coordenada aleatoria
                fila = random.randint(0, self.filas - 1)
                # Asegurar que cabe horizontalmente (columna + tamaño <= 10)
                col_max = self.columnas - tamano
                if col_max < 0: continue # Por seguridad, aunque con tamano <= 3 siempre cabe
                
                col = random.randint(0, col_max)
                
                if self.validar_posicion(fila, col, tamano):
                    nuevo_barco = Barco(tamano)
                    # Si paso la validacion, se crea un nuevo varco con el tamaño que toca de la lista barcos_a_colocar
                    self.flota.append(nuevo_barco)
                    # Colocar referencias al barco en el tablero
                    for i in range(tamano):
                        self.tablero[fila][col + i] = nuevo_barco
                    colocado = True

    def juego_terminado(self):
        """Devuelve True si todos los barcos han sido hundidos."""
        for barco in self.flota:
            if not barco.esta_hundido():
                return False
                # Si alguno NO esta hundido, devuelve False
        return True
        # Si todos estan hundidos, devuelve True

    def validar_posicion(self, fila, col, tamano):
        """
        Para comprobar si se puede colocar un barco de tal 'tamano' en esa posicion (fila, col) horizontalmente.
        Comprueba que no haya otros barcos en esas celdas.
        """
        for i in range(tamano):
            if self.tablero[fila][col + i] is not None:
                return False
            ## Si es None significa que hay agua, osea que si entra el barco
        return True

    def disparar(self, fila, col):
        """
        Procesa un disparo en la coordenada (fila, col).
        Retorna una tupla: (estado, barco_hundido)
        Hay tres estados posibles: "AGUA", "TOCADO", "HUNDIDO"
        barco_hundido: Objeto Barco si se hundió, None si no.
        """
        contenido = self.tablero[fila][col]
        
        if contenido is None:
            # Si en la posicion contenido hay agua (None)...
            self.disparos[fila][col] = "AGUA"
            return "AGUA", None
        
        # Si hay un barco (contenido es un objeto Barco)
        barco = contenido

        if self.disparos[fila][col] is None:
             barco.recibir_golpe()
        
        self.disparos[fila][col] = "TOCADO" # Estado provisional
        
        if barco.esta_hundido():
            # Actualizar estado de disparos para todas las celdas de este barco a "HUNDIDO"
            return "HUNDIDO", barco
        else:
            return "TOCADO", None

# -----------------------------------------------------------------------------
# INTERFAZ GRÁFICA (FRONTEND)
# -----------------------------------------------------------------------------

class InterfazBatallaNaval:
    """
    Maneja la ventana, botones y eventos del usuario usando tkinter.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Batalla Naval - Python POO")
        
        # Instancia de la lógica del juego
        self.juego = JuegoBatallaNaval()
        
        # Configuración de estilos
        self.color_agua = "#e0f7fa"    # Azul claro
        self.color_tocado = "#ffcdd2"  # Rojo claro
        self.color_fallo = "#0288d1" # Azul más fuerte para el acierto en agua (fallo)
        
        # Colores para barcos hundidos según tamaño
        self.color_hundido_3 = "#5D4037" # Marrón Oscuro
        self.color_hundido_2 = "#A5D6A7" # Verde Pastel
        self.color_hundido_1 = "#d32f2f" # Rojo Fuerte (Original)
        
        self.crear_widgets()

    def crear_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack()

        # Etiqueta de estado
        self.etiqueta_estado = tk.Label(
            main_frame, 
            text="¡Bienvenido! Selecciona una celda para disparar.",
            font=("Arial", 12, "bold"),
            pady=10
        )
        self.etiqueta_estado.grid(row=0, column=0, columnspan=11)

        # Encabezados de Columnas (1-10)
        for c in range(10):
            lbl = tk.Label(main_frame, text=str(c + 1), font=("Arial", 10, "bold"), width=4)
            lbl.grid(row=1, column=c + 1)

        # Encabezados de Filas (A-J) y Botones
        letras = "ABCDEFGHIJ"
        self.botones = [] # Matriz de botones para acceder por coordenadas

        for r in range(10):
            fila_botones = []
            # Letra de fila
            lbl = tk.Label(main_frame, text=letras[r], font=("Arial", 10, "bold"), width=4)
            lbl.grid(row=r + 2, column=0)

            for c in range(10):
                # Usamos lambda con valores por defecto para capturar r y c correctamente en el loop
                btn = tk.Button(
                    main_frame, 
                    width=4, 
                    height=2,
                    bg="#eceff1", # Gris muy claro inicial
                    command=lambda f=r, col=c: self.manejar_clic(f, col)
                )
                btn.grid(row=r + 2, column=c + 1)
                fila_botones.append(btn)
            self.botones.append(fila_botones)

    def manejar_clic(self, fila, columna):
        """
        Método llamado al hacer clic en un botón.
        Coordina la acción con la lógica del juego y actualiza la vista.
        """
        # Deshabilitar botón inmediatamente para evitar doble clic
        boton = self.botones[fila][columna]
        if boton['state'] == 'disabled':
            return

        # Llamar a la lógica
        resultado, barco = self.juego.disparar(fila, columna)

        # Actualizar UI según resultado
        if resultado == "AGUA":
            boton.config(bg=self.color_fallo, text="~", state="disabled")
            self.etiqueta_estado.config(text="¡Agua! Sigue intentando.", fg="blue")
            
        elif resultado == "TOCADO":
            boton.config(bg=self.color_tocado, text="X", state="disabled")
            self.etiqueta_estado.config(text="¡Tocado!", fg="orange")
            
        elif resultado == "HUNDIDO":
            boton.config(bg=self.color_hundido, text="X", state="disabled")
            self.etiqueta_estado.config(text=f"¡BARCO HUNDIDO! (Tamaño {barco.tamano})", fg="red")
            # Opcional: Si quisiéramos pintar todo el barco de rojo oscuro al hundirse,
            # tendríamos que buscar en el tablero dónde está ese barco y actualizar esos botones.
            # Por simplicidad del requerimiento, marcamos el último golpe.
            # Pero para mejor UX, vamos a recorrer el tablero y actualizar todos los botones de ese barco.
            self.resaltar_barco_hundido(barco)

            if self.juego.juego_terminado():
                messagebox.showinfo("Fin del Juego", "Juego finalizado! Se han hundido todos los barcos")
                self.deshabilitar_tablero()

    def resaltar_barco_hundido(self, barco):
        """
        Busca todas las celdas que contienen al barco hundido y las pone en el color correspondiente.
        """
        color = self.color_hundido_1 # Default
        if barco.tamano == 3:
            color = self.color_hundido_3
        elif barco.tamano == 2:
            color = self.color_hundido_2
            
        for f in range(10):
            for c in range(10):
                if self.juego.tablero[f][c] == barco:
                    self.botones[f][c].config(bg=color, text="X")

    def deshabilitar_tablero(self):
        """Deshabilita todos los botones del tablero al finalizar el juego."""
        for f in range(10):
            for c in range(10):
                self.botones[f][c].config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazBatallaNaval(root)
    root.mainloop()
