import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.geometry("300x400")
        self.ventana.resizable(False, False)
        
        # Variables para el cálculo
        self.numero_actual = ""
        self.numero_anterior = ""
        self.operador = ""
        self.resultado = 0
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Pantalla de visualización
        self.pantalla = tk.Entry(
            self.ventana,
            font=("Arial", 20),
            justify="right",
            state="readonly",
            width=15
        )
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        # Configurar el grid para que los botones se expandan
        for i in range(4):
            self.ventana.grid_columnconfigure(i, weight=1)
        
        # Botones
        botones = [
            ('C', 1, 0), ('%', 1, 1), ('/', 1, 2), ('*', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('+', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('=', 4, 3),
            ('0', 5, 0), ('.', 5, 2)
        ]
        
        for texto, fila, columna in botones:
            if texto == '0':
                btn = tk.Button(
                    self.ventana,
                    text=texto,
                    font=("Arial", 16),
                    command=lambda t=texto: self.click_boton(t),
                    height=2
                )
                btn.grid(row=fila, column=columna, columnspan=2, padx=2, pady=2, sticky="ew")
            else:
                btn = tk.Button(
                    self.ventana,
                    text=texto,
                    font=("Arial", 16),
                    command=lambda t=texto: self.click_boton(t),
                    height=2
                )
                btn.grid(row=fila, column=columna, padx=2, pady=2, sticky="ew")
    
    def click_boton(self, valor):
        if valor.isdigit() or valor == '.':
            self.numero_actual += valor
            self.actualizar_pantalla(self.numero_actual)
        elif valor in ['+', '-', '*', '/', '%']:
            if self.numero_actual:
                if self.numero_anterior and self.operador:
                    self.calcular()
                self.numero_anterior = self.numero_actual
                self.numero_actual = ""
                self.operador = valor
        elif valor == '=':
            if self.numero_anterior and self.numero_actual and self.operador:
                self.calcular()
        elif valor == 'C':
            self.limpiar()
    
    def calcular(self):
        try:
            if self.operador == '+':
                resultado = float(self.numero_anterior) + float(self.numero_actual)
            elif self.operador == '-':
                resultado = float(self.numero_anterior) - float(self.numero_actual)
            elif self.operador == '*':
                resultado = float(self.numero_anterior) * float(self.numero_actual)
            elif self.operador == '/':
                if float(self.numero_actual) == 0:
                    messagebox.showerror("Error", "No se puede dividir por cero")
                    return
                resultado = float(self.numero_anterior) / float(self.numero_actual)
            elif self.operador == '%':
                resultado = float(self.numero_anterior) % float(self.numero_actual)
            
            self.numero_actual = str(resultado)
            self.actualizar_pantalla(self.numero_actual)
            self.numero_anterior = ""
            self.operador = ""
            
        except Exception as e:
            messagebox.showerror("Error", "Error en el cálculo")
            self.limpiar()
    
    def actualizar_pantalla(self, valor):
        self.pantalla.config(state="normal")
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, valor)
        self.pantalla.config(state="readonly")
    
    def limpiar(self):
        self.numero_actual = ""
        self.numero_anterior = ""
        self.operador = ""
        self.actualizar_pantalla("0")
    
    def ejecutar(self):
        self.ventana.mainloop()

# Crear y ejecutar la calculadora
if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.ejecutar()
