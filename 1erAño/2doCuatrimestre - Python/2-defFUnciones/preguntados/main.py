import tkinter as tk
from tkinter import messagebox
import random
import time


def iniciar_juego():
    frame_inicio.pack_forget()
    frame_juego.pack(fill="both", expand=True)
    actualizar_puntaje()
    lbl_turno.config(text=f"Turno de: {jugadores[0]}")

def elegir_categoria(cat):
    global pregunta_actual, opciones_actuales, respuesta_correcta
    pregunta_actual, opciones_actuales, respuesta_correcta = random.choice(preguntas[cat])
    lbl_categoria.config(text=f"Categoría: {cat}")
    lbl_pregunta.config(text=pregunta_actual)
    color_categoria = colores_categoria[cat]
    for i, boton in enumerate(botones_opciones):
        boton.config(text=opciones_actuales[i], state="normal", bg=color_categoria, fg="white")

def verificar_respuesta(opcion):
    global turno
    jugador = jugadores[turno % 2]
    if opcion == respuesta_correcta:
        mensajes_correctos = [
            f"¡EXCELENTE {jugador}! 🎯",
            f"¡PERFECTO {jugador}! 🌟",
            f"¡INCREÍBLE {jugador}! 🚀",
            f"¡FANTÁSTICO {jugador}! ⭐"
        ]
        messagebox.showinfo("✅ ¡CORRECTO!", random.choice(mensajes_correctos))
        puntaje[jugador] += 1
    else:
        mensajes_incorrectos = [
            f"¡Ups! La respuesta correcta era: {respuesta_correcta}",
            f"¡Casi! La respuesta era: {respuesta_correcta}",
            f"¡No te preocupes! Era: {respuesta_correcta}",
            f"¡Siguiente vez será! La respuesta: {respuesta_correcta}"
        ]
        messagebox.showerror("❌ INCORRECTO", random.choice(mensajes_incorrectos))
    actualizar_puntaje()

    
    total_preguntas_jugadas = (turno + 1)
    if total_preguntas_jugadas >= rondas_por_jugador * 2:
        if puntaje[jugadores[0]] > puntaje[jugadores[1]]:
            mostrar_insignia(jugadores[0])
            return
        elif puntaje[jugadores[1]] > puntaje[jugadores[0]]:
            mostrar_insignia(jugadores[1])
            return
        else:
            mostrar_empate()
            return

    turno += 1
    lbl_turno.config(text=f"Turno de: {jugadores[turno % 2]}")
    lbl_pregunta.config(text="Selecciona una categoría para continuar")
    for boton in botones_opciones:
        boton.config(state="disabled", bg="#2c2c54")

def actualizar_puntaje():
    lbl_puntaje.config(text=f"{jugadores[0]}: {puntaje[jugadores[0]]} | {jugadores[1]}: {puntaje[jugadores[1]]}")

def mostrar_insignia(ganador):
    frame_juego.pack_forget()
    frame_insignia.pack(fill="both", expand=True)
    lbl_ganador.config(text=f"🏆 ¡{ganador} ES EL MAESTRO DE LA TECNOLOGÍA! 🏆")
    btn_reiniciar.pack(pady=20)
    animar_insignia()

def mostrar_empate():
    frame_juego.pack_forget()
    frame_insignia.pack(fill="both", expand=True)
    lbl_ganador.config(text="🤝 ¡EMPATE TECNOLÓGICO! Ambos son verdaderos expertos 🤝")
    btn_reiniciar.pack(pady=20)
    animar_insignia()

def animar_insignia():
    colores_animacion = ["#FFD700", "#FF6347", "#32CD32", "#87CEEB", "#FFD700", "#FF6347", "#32CD32", "#87CEEB"]
    for i in range(8):
        canvas_insignia.itemconfig(circulo, fill=colores_animacion[i])
        ventana.update()
        time.sleep(0.15)

def reiniciar_juego():
    global puntaje, turno
    puntaje = {jugadores[0]: 0, jugadores[1]: 0}
    turno = 0
    frame_insignia.pack_forget()
    frame_juego.pack(fill="both", expand=True)
    lbl_puntaje.config(text=f"{jugadores[0]}: 0 | {jugadores[1]}: 0")
    lbl_turno.config(text=f"Turno de: {jugadores[0]}")
    lbl_pregunta.config(text="Selecciona una categoría para comenzar")
    lbl_categoria.config(text="")
    for boton in botones_opciones:
        boton.config(text="", state="disabled", bg="#2c2c54")


preguntas = {
    "Hardware": [
        ("¿Qué componente es el 'cerebro' de la computadora?", ["CPU", "GPU", "RAM", "Disco duro"], "CPU"),
        ("¿Cuál es la función principal de la RAM?", ["Almacenamiento temporal", "Almacenamiento permanente", "Procesamiento gráfico", "Conectividad"], "Almacenamiento temporal"),
        ("¿Qué tipo de memoria es más rápida?", ["Cache L1", "RAM DDR4", "SSD", "HDD"], "Cache L1"),
        ("¿Cuántos pines tiene una memoria RAM DDR4?", ["288", "240", "184", "168"], "288"),
        ("¿Qué significa GPU?", ["Unidad de Procesamiento Gráfico", "Gestión de Procesos Unidos", "Grupo de Procesadores Únicos", "Generación de Programas Unidos"], "Unidad de Procesamiento Gráfico"),
        ("¿Cuál es el puerto más común para conectar monitores?", ["HDMI", "USB", "Ethernet", "VGA"], "HDMI"),
        ("¿Qué componente controla la velocidad del procesador?", ["Reloj del sistema", "Ventilador", "Fuente de poder", "Chipset"], "Reloj del sistema"),
        ("¿Cuántos bits tiene un byte?", ["8", "16", "32", "64"], "8"),
        ("¿Qué tipo de almacenamiento es más rápido?", ["NVMe SSD", "SATA SSD", "HDD", "CD-ROM"], "NVMe SSD"),
        ("¿Cuál es la función de la placa madre?", ["Conectar todos los componentes", "Procesar datos", "Almacenar información", "Mostrar imágenes"], "Conectar todos los componentes"),
    ],
    "Software": [
        ("¿Qué es un sistema operativo?", ["Software que gestiona el hardware", "Programa de diseño", "Antivirus", "Navegador web"], "Software que gestiona el hardware"),
        ("¿Cuál es el kernel de Linux?", ["Núcleo del sistema", "Interfaz gráfica", "Navegador", "Editor de texto"], "Núcleo del sistema"),
        ("¿Qué significa API?", ["Interfaz de Programación de Aplicaciones", "Algoritmo de Procesamiento Inteligente", "Archivo de Programación Integrada", "Acceso a Programas Informáticos"], "Interfaz de Programación de Aplicaciones"),
        ("¿Qué es un compilador?", ["Traduce código a lenguaje máquina", "Ejecuta programas", "Diseña interfaces", "Administra memoria"], "Traduce código a lenguaje máquina"),
        ("¿Cuál es la diferencia entre software libre y propietario?", ["Licencia de uso", "Velocidad de ejecución", "Tamaño del archivo", "Calidad gráfica"], "Licencia de uso"),
        ("¿Qué es un algoritmo?", ["Conjunto de pasos para resolver un problema", "Tipo de hardware", "Lenguaje de programación", "Base de datos"], "Conjunto de pasos para resolver un problema"),
        ("¿Qué significa IDE?", ["Entorno de Desarrollo Integrado", "Interfaz de Datos Electrónicos", "Identificador de Dispositivos", "Instituto de Desarrollo"], "Entorno de Desarrollo Integrado"),
        ("¿Qué es un bug en programación?", ["Error en el código", "Característica nueva", "Tipo de variable", "Función especial"], "Error en el código"),
        ("¿Cuál es la función de un depurador?", ["Encontrar errores en el código", "Compilar programas", "Diseñar interfaces", "Administrar archivos"], "Encontrar errores en el código"),
        ("¿Qué es la recursión?", ["Función que se llama a sí misma", "Tipo de bucle", "Estructura de datos", "Algoritmo de ordenamiento"], "Función que se llama a sí misma"),
    ],
    "Redes y Conectividad": [
        ("¿Qué significa IP?", ["Protocolo de Internet", "Interfaz de Programación", "Identificador de Procesos", "Instituto de Programación"], "Protocolo de Internet"),
        ("¿Cuál es la velocidad máxima del WiFi 6?", ["9.6 Gbps", "3.5 Gbps", "1.3 Gbps", "600 Mbps"], "9.6 Gbps"),
        ("¿Qué puerto usa HTTP por defecto?", ["80", "443", "21", "25"], "80"),
        ("¿Qué significa DNS?", ["Sistema de Nombres de Dominio", "Datos de Navegación Segura", "Dispositivo de Red Simple", "Dirección de Nodos"], "Sistema de Nombres de Dominio"),
        ("¿Cuál es la diferencia entre IPv4 e IPv6?", ["Longitud de dirección", "Velocidad de conexión", "Tipo de cable", "Protocolo de seguridad"], "Longitud de dirección"),
        ("¿Qué hace un router?", ["Dirige el tráfico de red", "Almacena datos", "Procesa información", "Muestra contenido"], "Dirige el tráfico de red"),
        ("¿Cuántos bits tiene una dirección IPv4?", ["32", "64", "128", "16"], "32"),
        ("¿Qué significa VPN?", ["Red Privada Virtual", "Verificación de Protocolos", "Ventana de Programación", "Validación de Nodos"], "Red Privada Virtual"),
        ("¿Cuál es el protocolo de correo electrónico?", ["SMTP", "HTTP", "FTP", "SSH"], "SMTP"),
        ("¿Qué hace un firewall?", ["Filtra el tráfico de red", "Acelera la conexión", "Almacena contraseñas", "Diseña páginas web"], "Filtra el tráfico de red"),
    ],
    "Programación": [
        ("¿Qué lenguaje es más usado en desarrollo web?", ["JavaScript", "Python", "C++", "Java"], "JavaScript"),
        ("¿Qué significa HTML?", ["Lenguaje de Marcado de Hipertexto", "Herramienta de Manejo de Texto", "Hipervínculo de Marcado", "Host de Transferencia"], "Lenguaje de Marcado de Hipertexto"),
        ("¿Cuál es la diferencia entre '==' y '===' en JavaScript?", ["Comparación estricta", "Velocidad de ejecución", "Tipo de variable", "Alcance de función"], "Comparación estricta"),
        ("¿Qué es Git?", ["Sistema de control de versiones", "Lenguaje de programación", "Base de datos", "Servidor web"], "Sistema de control de versiones"),
        ("¿Cuál es la función de CSS?", ["Estilizar páginas web", "Crear bases de datos", "Procesar datos", "Administrar servidores"], "Estilizar páginas web"),
        ("¿Qué significa MVC?", ["Modelo-Vista-Controlador", "Manejo de Variables Complejas", "Método de Validación", "Motor de Visualización"], "Modelo-Vista-Controlador"),
        ("¿Qué es una variable global?", ["Variable accesible en todo el programa", "Variable rápida", "Variable segura", "Variable temporal"], "Variable accesible en todo el programa"),
        ("¿Cuál es la función de un framework?", ["Simplificar el desarrollo", "Acelerar el hardware", "Comprimir archivos", "Diseñar interfaces"], "Simplificar el desarrollo"),
        ("¿Qué significa REST?", ["Transferencia de Estado Representacional", "Recuperación de Estado Temporal", "Registro de Eventos", "Red de Servicios"], "Transferencia de Estado Representacional"),
        ("¿Qué es un array?", ["Estructura de datos ordenada", "Tipo de función", "Algoritmo de búsqueda", "Método de compresión"], "Estructura de datos ordenada"),
    ]
}


jugadores = ["💻 Tech Master 1", "⚡ Tech Master 2"]
puntaje = {jugadores[0]: 0, jugadores[1]: 0}
turno = 0
pregunta_actual = None
respuesta_correcta = None
rondas_por_jugador = 3  


ventana = tk.Tk()
ventana.title("💻 TECH TRIVIA - HARDWARE & SOFTWARE 💻")
ventana.geometry("1200x800")
ventana.config(bg="#1a1a2e")

colores_categoria = {
    "Hardware": "#FF6B35",
    "Software": "#4ECDC4",
    "Redes y Conectividad": "#45B7D1",
    "Programación": "#96CEB4"
}


frame_inicio = tk.Frame(ventana, bg="#16213e")
frame_inicio.pack(fill="both", expand=True)
tk.Label(frame_inicio, text="💻 TECH TRIVIA 💻", font=("Impact", 32, "bold"), fg="#FFD700", bg="#16213e").pack(pady=80)
tk.Label(frame_inicio, text="¡Demuestra tu conocimiento en tecnología!", font=("Arial", 18, "italic"), fg="#87CEEB", bg="#16213e").pack(pady=10)
tk.Button(frame_inicio, text="🚀 COMENZAR AVENTURA 🚀", font=("Arial", 18, "bold"), bg="#FF6347", fg="white", width=25, height=3, command=iniciar_juego, relief="raised", bd=5).pack(pady=30)


frame_juego = tk.Frame(ventana, bg="#0f0f23")

lbl_turno = tk.Label(frame_juego, text="", font=("Arial", 20, "bold"), bg="#0f0f23", fg="#FFD700")
lbl_turno.pack(pady=20)

frame_categorias = tk.Frame(frame_juego, bg="#0f0f23")
frame_categorias.pack(pady=15)

for cat in preguntas.keys():
    tk.Button(frame_categorias, text=cat, width=22, height=3, bg=colores_categoria[cat], fg="white", font=("Arial", 13, "bold"),
              command=lambda c=cat: elegir_categoria(c), relief="raised", bd=3).pack(side="left", padx=12)

lbl_categoria = tk.Label(frame_juego, text="", font=("Arial", 16, "italic"), bg="#0f0f23", fg="#87CEEB")
lbl_categoria.pack(pady=10)

lbl_pregunta = tk.Label(frame_juego, text="Selecciona una categoría para comenzar", font=("Arial", 16), wraplength=1000, bg="#0f0f23", fg="white")
lbl_pregunta.pack(pady=25)

frame_opciones = tk.Frame(frame_juego, bg="#0f0f23")
frame_opciones.pack()

botones_opciones = []
for i in range(4):
    b = tk.Button(frame_opciones, text="", width=60, height=3, state="disabled", bg="#2c2c54", fg="white",
                  font=("Arial", 14), command=lambda i=i: verificar_respuesta(botones_opciones[i].cget("text")), relief="raised", bd=2)
    b.pack(pady=8)
    botones_opciones.append(b)

lbl_puntaje = tk.Label(frame_juego, text=f"{jugadores[0]}: 0 | {jugadores[1]}: 0", font=("Arial", 16, "bold"), bg="#0f0f23", fg="#FFD700")
lbl_puntaje.pack(pady=15)


frame_insignia = tk.Frame(ventana, bg="#1a1a2e")
lbl_ganador = tk.Label(frame_insignia, text="", font=("Impact", 28, "bold"), bg="#1a1a2e", fg="#FFD700")
lbl_ganador.pack(pady=40)
canvas_insignia = tk.Canvas(frame_insignia, width=250, height=250, bg="#1a1a2e", highlightthickness=0)
canvas_insignia.pack()
circulo = canvas_insignia.create_oval(75, 75, 175, 175, fill="#FFD700", outline="#FF6347", width=6)
canvas_insignia.create_text(125, 125, text="🏆", font=("Arial", 50))

btn_reiniciar = tk.Button(frame_insignia, text="🔄 JUGAR DE NUEVO 🔄", bg="#32CD32", fg="white", font=("Arial", 16, "bold"), width=20, height=2, command=reiniciar_juego, relief="raised", bd=4)
btn_salir = tk.Button(frame_insignia, text="🚪 SALIR", bg="#DC143C", fg="white", font=("Arial", 16, "bold"), width=15, height=2, command=ventana.destroy, relief="raised", bd=4)
btn_salir.pack(pady=20)

ventana.mainloop()