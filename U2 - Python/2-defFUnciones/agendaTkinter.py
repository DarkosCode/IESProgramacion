import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Agenda")

# etiqueta = tk.Label(ventana, text="Agenda de contactos")
# etiqueta.pack()

nombreLabel = tk.Label(ventana, text="Nombre")
input_Nombre = tk.Entry(ventana)
telefLabel = tk.Label(ventana, text="Telefono")
input_Telefono = tk.Entry(ventana)

##Tree View (vista de tablas)
TreeAgenda = ttk.Treeview(ventana, columns=('ID', 'Nombre', 'Telefono'), show='headings')
TreeAgenda.heading('ID', text='ID')
TreeAgenda.heading('Nombre', text='Nombre')
TreeAgenda.heading('Telefono', text='Telefono')

## Funcion de añadir contacto
contactos = []
def añadirContacto():
    nombre = input_Nombre.get()
    telefono = input_Telefono.get()
    idUsuario = len(contactos)+1 #autoincremental
    contactos.append([idUsuario, nombre, telefono])
    print(contactos)

## Boton
botonAñadir = tk.Button(ventana, text="Añadir", command=añadirContacto)

## Con los .pack() los 'metemos dentro' de las ventanas
nombreLabel.pack()
input_Nombre.pack(pady=10)

telefLabel.pack()
input_Telefono.pack(pady=10) 

botonAñadir.pack(pady=10)

TreeAgenda.pack()


ventana.mainloop(
    
)