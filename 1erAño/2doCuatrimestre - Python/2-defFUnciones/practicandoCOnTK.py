import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("1300x1000")

# etiqueta = tk.Label(ventana, text='Esta es mi primera ventana con TK', font=("CALIBRI", 20))
# etiqueta.pack()

def mostrar_texto():
    texto = entrada.get()
    etiqueta_resultado.config(text=texto)

# 2. Crear campo de entrada
entrada = tk.Entry(ventana, width=25)
entrada.pack(pady=10)

# 3. Crear botón
boton = tk.Button(ventana, text="Mostrar", command=mostrar_texto)
boton.pack(pady=5)

# 4. Crear etiqueta donde se mostrará el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)


ventana.mainloop()