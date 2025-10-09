import tkinter as tk
import tkinter.messagebox as messagebox
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
TreeAgenda.column('Nombre', width=120, anchor='center', stretch=True)      # estira
TreeAgenda.column('Telefono', width=190, anchor='center', stretch=True)

## Funcion de añadir contacto
contactos = []

def existe_contacto(nombre: str, telefono: str) -> bool:
    n = nombre.strip().lower()
    t = telefono.strip()
    return any(c[1].strip().lower() == n and c[2].strip() == t for c in contactos)

def añadirContacto():
    nombre   = input_Nombre.get()
    telefono = input_Telefono.get()

    if not (nombre and telefono):
        messagebox.showwarning("Campos Vacíos", "Debes completar todos los campos!")
        return
    if len(telefono) != 10:
        messagebox.showerror("Cantidad de dígitos", "El Nº debe tener 10 dígitos")
        return
    if existe_contacto(nombre, telefono):
        messagebox.showerror("Contacto repetido", "El contacto ya existe en la agenda")
        return

    idUsuario = len(contactos) + 1
    contactos.append([idUsuario, nombre, telefono])
    TreeAgenda.insert('', 'end', values=(idUsuario, nombre, telefono))
    limpiar_campos()
    
    
def limpiar_campos():
    input_Nombre.delete(0, tk.END)
    input_Telefono.delete(0, tk.END)
    input_Nombre.focus_set()   # opcional: vuelve a enfocar el primer campo
    
# Nombre y funcion más descriptiva para borrar todas las filas del Treeview
def clear_treeview():
    ##*Borra todas las filas del Treeview `TreeAgenda`
    for elem in TreeAgenda.get_children():
        TreeAgenda.delete(elem)

# Mantener `update` como alias por compatibilidad (por si se usa en otro sitio)
#? update = clear_treeview

def borrarContacto():
    seleccionado = TreeAgenda.selection()
    
    if not seleccionado:
        messagebox.showwarning("Selección vacía", "Debes seleccionar un contacto para borrar.")
        return

    for item in seleccionado:
        valores = TreeAgenda.item(item)['values']   # ('1', 'Luis', '2616314791') => strings
        id_borrar = int(valores[0])                 # <-- convertir a int

        # borrar del modelo
        contactos[:] = [c for c in contactos if c[0] != id_borrar]

        # borrar de la vista
        TreeAgenda.delete(item)

    messagebox.showinfo("Contacto borrado", "El contacto ha sido borrado exitosamente.")
    
def editarContacto():
    pass

## Boton
botonAñadir = tk.Button(ventana, text="Añadir", command=añadirContacto)
## Borrar
botonBorrar = tk.Button(ventana, text="Borrar", command=borrarContacto)
# Botón para limpiar la vista del Treeview
botonEditar = tk.Button(ventana, text="Editar", command=editarContacto)
# Botón para limpiar la vista del Treeview
botonLimpiar = tk.Button(ventana, text="Limpiar", command=clear_treeview)

## Con los .pack() los 'metemos dentro' de las ventanas
nombreLabel.pack()
input_Nombre.pack(pady=10)

telefLabel.pack()
input_Telefono.pack(pady=10) 

botonAñadir.pack(pady=10)
botonBorrar.pack(pady=10)
botonLimpiar.pack(pady=10)

TreeAgenda.pack(fill="both", expand=True, padx=10, pady=10)


ventana.mainloop()