import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk

# Diseño y colores hechos con Cursor
COLORES = {
    'fondo_principal': '#2C3E50',      # Azul oscuro elegante
    'fondo_secundario': '#34495E',     # Gris azulado
    'fondo_claro': '#ECF0F1',          # Gris muy claro
    'accent': '#3498DB',               # Azul brillante
    'accent_hover': '#2980B9',         # Azul más oscuro para hover
    'success': '#27AE60',              # Verde para añadir
    'warning': '#F39C12',              # Naranja para editar
    'danger': '#E74C3C',               # Rojo para borrar
    'texto_principal': '#2C3E50',      # Texto principal
    'texto_claro': '#FFFFFF',          # Texto claro
    'borde': '#BDC3C7'                 # Borde gris
}

ventana = tk.Tk()
ventana.geometry("1000x900")
ventana.title("Agenda de Contactos")
ventana.configure(bg=COLORES['fondo_principal'])


style = ttk.Style()
style.theme_use('clam')
style.configure('Treeview', 
                background=COLORES['fondo_claro'],
                foreground=COLORES['texto_principal'],
                fieldbackground=COLORES['fondo_claro'],
                rowheight=35,
                font=('Segoe UI', 10))
style.configure('Treeview.Heading',
                background=COLORES['accent'],
                foreground=COLORES['texto_claro'],
                font=('Segoe UI', 11, 'bold'))

# Frame principal con padding
main_frame = tk.Frame(ventana, bg=COLORES['fondo_principal'], padx=20, pady=20)
main_frame.pack(fill='both', expand=True)

# Título principal
titulo = tk.Label(main_frame, 
                 text="Agenda de Contactos", 
                 font=('Segoe UI', 24, 'bold'),
                 fg=COLORES['texto_claro'],
                 bg=COLORES['fondo_principal'])
titulo.pack(pady=(0, 20))

# Frame para formulario de entrada
form_frame = tk.Frame(main_frame, bg=COLORES['fondo_secundario'], relief='raised', bd=2)
form_frame.pack(fill='x', pady=(0, 20), padx=10)

# Configurar grid para el formulario
form_frame.grid_columnconfigure(1, weight=1)

# Labels y inputs con mejor estilo
nombreLabel = tk.Label(form_frame, 
                      text="Nombre:", 
                      font=('Segoe UI', 12, 'bold'),
                      fg=COLORES['texto_claro'],
                      bg=COLORES['fondo_secundario'])
nombreLabel.grid(row=0, column=0, sticky='w', padx=15, pady=10)

input_Nombre = tk.Entry(form_frame, 
                       font=('Segoe UI', 11),
                       relief='flat',
                       bd=5,
                       bg=COLORES['fondo_claro'],
                       fg=COLORES['texto_principal'])
input_Nombre.grid(row=0, column=1, sticky='ew', padx=(0, 15), pady=10)

telefLabel = tk.Label(form_frame, 
                     text="Teléfono:", 
                     font=('Segoe UI', 12, 'bold'),
                     fg=COLORES['texto_claro'],
                     bg=COLORES['fondo_secundario'])
telefLabel.grid(row=1, column=0, sticky='w', padx=15, pady=10)

input_Telefono = tk.Entry(form_frame, 
                         font=('Segoe UI', 11),
                         relief='flat',
                         bd=5,
                         bg=COLORES['fondo_claro'],
                         fg=COLORES['texto_principal'])
input_Telefono.grid(row=1, column=1, sticky='ew', padx=(0, 15), pady=10)

# Frame para la tabla de contactos
table_frame = tk.Frame(main_frame, bg=COLORES['fondo_principal'])
table_frame.pack(fill='both', expand=True, pady=(0, 10))

# Título de la tabla
tabla_titulo = tk.Label(table_frame, 
                       text="Lista de Contactos", 
                       font=('Segoe UI', 14, 'bold'),
                       fg=COLORES['texto_claro'],
                       bg=COLORES['fondo_principal'])
tabla_titulo.pack(pady=(0, 10))

# Tree View (vista de tablas) con mejor estilo
TreeAgenda = ttk.Treeview(table_frame, columns=('ID', 'Nombre', 'Telefono'), show='headings')

TreeAgenda.heading('ID', text='ID')
TreeAgenda.heading('Nombre', text='Nombre')
TreeAgenda.heading('Telefono', text='Teléfono')

# Columnas: ancho y alineación del contenido
TreeAgenda.column('ID', width=80, anchor='center', stretch=False)     # no estira
TreeAgenda.column('Nombre', width=200, anchor='center', stretch=True)      # estira
TreeAgenda.column('Telefono', width=200, anchor='center', stretch=True)

# array que guarda contactos
contactos = []

def existe_contacto(nombre: str, telefono: str) -> bool:
    n = nombre.strip().lower()
    t = telefono.strip()
    return any(c[1].strip().lower() == n and c[2].strip() == t for c in contactos)

## Funcion de añadir contacto
def añadirContacto():
    nombre   = input_Nombre.get().strip()
    telefono = input_Telefono.get().strip()

    if not (nombre and telefono):
        messagebox.showwarning("Campos Vacíos", "Debes completar todos los campos!")
        return
    if len(telefono) != 10:
        messagebox.showerror("Error de Teléfono", "El número debe tener exactamente 10 dígitos")
        return
    if existe_contacto(nombre, telefono):
        messagebox.showerror("Contacto Duplicado", "Este contacto ya existe en la agenda")
        return

    idUsuario = len(contactos) + 1
    contactos.append([idUsuario, nombre, telefono])
    TreeAgenda.insert('', 'end', values=(idUsuario, nombre, telefono))
    limpiar_campos()
    messagebox.showinfo("Éxito", f"Contacto '{nombre}' añadido correctamente!")
    
    
def limpiar_campos():
    input_Nombre.delete(0, tk.END)
    input_Telefono.delete(0, tk.END)
    input_Nombre.focus_set()   # opcional: vuelve a enfocar el primer campo
    
# Función mejorada para limpiar toda la agenda
def clear_treeview():
    if not contactos:
        messagebox.showinfo("ℹAgenda Vacía", "La agenda ya está vacía.")
        return
    
    respuesta = messagebox.askyesno("🧹 Limpiar Agenda", 
                                   f"¿Estás seguro de que quieres eliminar todos los {len(contactos)} contactos?")
    
    if respuesta:
        # Borrar todas las filas del Treeview
        for elem in TreeAgenda.get_children():
            TreeAgenda.delete(elem)
        
        # Limpiar el array de contactos
        contactos.clear()
        
        messagebox.showinfo("Agenda Limpiada", "Todos los contactos han sido eliminados.")

# Mantener `update` como alias por compatibilidad (por si se usa en otro sitio)
#? update = clear_treeview

def borrarContacto():
    seleccionado = TreeAgenda.selection()
    
    if not seleccionado:
        messagebox.showwarning("Sin Selección", "Debes seleccionar un contacto para borrar.")
        return

    # Confirmar eliminación
    valores = TreeAgenda.item(seleccionado[0])['values']
    nombre_contacto = valores[1]
    
    respuesta = messagebox.askyesno("🗑️ Confirmar Eliminación", 
                                   f"¿Estás seguro de que quieres eliminar el contacto '{nombre_contacto}'?")
    
    if not respuesta:
        return

    for item in seleccionado:
        valores = TreeAgenda.item(item)['values']   # ('1', 'Luis', '2616314791') => strings
        id_borrar = int(valores[0])                 # <-- convertir a int

        # borrar del modelo
        contactos[:] = [c for c in contactos if c[0] != id_borrar]

        # borrar de la vista
        TreeAgenda.delete(item)

    messagebox.showinfo(" Contacto Eliminado", f"El contacto '{nombre_contacto}' ha sido eliminado exitosamente.")
    
def editarContacto():
    seleccionado = TreeAgenda.selection()
    
    if not seleccionado:
        messagebox.showwarning(" Sin Selección", "Debes seleccionar un contacto para editar.")
        return

    for item in seleccionado:
        valores = TreeAgenda.item(item)['values'] 
        id_editar = int(valores[0])
        nuevo_nombre = input_Nombre.get().strip()
        nuevo_telefono = input_Telefono.get().strip()

        if not (nuevo_nombre and nuevo_telefono):
            messagebox.showwarning(" Campos Vacíos", "Debes completar todos los campos para editar!")
            return
        if len(nuevo_telefono) != 10:
            messagebox.showerror("Error de Teléfono", "El número debe tener exactamente 10 dígitos")
            return

        # Actualizar en el modelo
        for c in contactos:
            if c[0] == id_editar:
                c[1] = nuevo_nombre
                c[2] = nuevo_telefono
                break

        # Actualizar en la vista
        TreeAgenda.item(item, values=(id_editar, nuevo_nombre, nuevo_telefono))

    messagebox.showinfo("Contacto Editado", f"El contacto ha sido editado exitosamente.")

# Frame para botones con mejor diseño
botonFrame = tk.Frame(main_frame, bg=COLORES['fondo_principal'])
botonFrame.pack(pady=(10, 20), fill='x')

# Función para crear botones con estilo moderno
def crear_boton(parent, text, command, color):
    return tk.Button(parent, 
                    text=text,
                    command=command,
                    font=('Segoe UI', 11, 'bold'),
                    bg=color,
                    fg=COLORES['texto_claro'],
                    relief='flat',
                    bd=0,
                    padx=20,
                    pady=10,
                    cursor='hand2',
                    activebackground=COLORES['accent_hover'])

# Botones con colores temáticos
botonAñadir = crear_boton(botonFrame, "Añadir", añadirContacto, COLORES['success'])
botonBorrar = crear_boton(botonFrame, "Borrar", borrarContacto, COLORES['danger'])
botonLimpiar = crear_boton(botonFrame, "Limpiar Todo", clear_treeview, COLORES['warning'])
botonEditar = crear_boton(botonFrame, "Editar", editarContacto, COLORES['accent'])

# Organizar botones en grid para mejor distribución
botonAñadir.grid(row=0, column=0, padx=8, pady=5, sticky='ew')
botonBorrar.grid(row=0, column=1, padx=8, pady=5, sticky='ew')
botonLimpiar.grid(row=0, column=2, padx=8, pady=5, sticky='ew')
botonEditar.grid(row=0, column=3, padx=8, pady=5, sticky='ew')

# Configurar columnas para que se distribuyan uniformemente
for i in range(4):
    botonFrame.grid_columnconfigure(i, weight=1)

# Pack del Treeview con mejor estilo
TreeAgenda.pack(fill="both", expand=True, padx=10, pady=10)

# Añadir scrollbar para la tabla
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=TreeAgenda.yview)
TreeAgenda.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Configurar eventos de teclado para mejor UX
def on_enter_key(event):
    añadirContacto()

def on_escape_key(event):
    limpiar_campos()

# Vincular eventos de teclado
ventana.bind('<Return>', on_enter_key)
ventana.bind('<Escape>', on_escape_key)

# Configurar el foco inicial
input_Nombre.focus_set()

# Añadir información de estado en la parte inferior
status_frame = tk.Frame(main_frame, bg=COLORES['fondo_secundario'], height=30)
status_frame.pack(fill='x', pady=(10, 0))

status_label = tk.Label(status_frame, 
                       text="Consejo: Usa Enter para añadir contacto, Escape para limpiar campos",
                       font=('Segoe UI', 9),
                       fg=COLORES['texto_claro'],
                       bg=COLORES['fondo_secundario'])
status_label.pack(pady=5)

# Centrar la ventana en la pantalla
ventana.update_idletasks()
width = ventana.winfo_width()
height = ventana.winfo_height()
x = (ventana.winfo_screenwidth() // 2) - (width // 2)
y = (ventana.winfo_screenheight() // 2) - (height // 2)
ventana.geometry(f'{width}x{height}+{x}+{y}')

ventana.mainloop()