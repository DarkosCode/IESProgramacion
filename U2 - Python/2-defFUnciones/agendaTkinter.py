import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("1000x800")
ventana.title("Agenda")

# Ajuste de estilo: evitar solapamiento de filas en Treeview
style = ttk.Style()
style.configure('Treeview', rowheight=32)

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

# Columnas: ancho y alineación del contenido
TreeAgenda.column('ID', width=60, anchor='center', stretch=False)     # no estira
TreeAgenda.column('Nombre', width=120, anchor='w', stretch=True)      # estira
TreeAgenda.column('Telefono', width=190, anchor='center', stretch=True)

## Funcion de añadir contacto
contactos = []
def añadirContacto():

    nombre = input_Nombre.get()
    telefono = input_Telefono.get()
    if len(telefono) != 10:
        from tkinter import messagebox
        messagebox.showerror("Error", "El N° debe tener 10 dígitos")
        return
    idUsuario = len(contactos) + 1  # autoincremental
    contactos.append([idUsuario, nombre, telefono])
    TreeAgenda.insert('', 'end', values=(idUsuario, nombre, telefono))


## Boton
botonAñadir = tk.Button(ventana, text="Añadir", command=añadirContacto)

## Con los .pack() los 'metemos dentro' de las ventanas
nombreLabel.pack()
input_Nombre.pack(pady=10)

telefLabel.pack()
input_Telefono.pack(pady=10) 

botonAñadir.pack(pady=10)

TreeAgenda.pack(fill="both", expand=True, padx=10, pady=10)


ventana.mainloop()