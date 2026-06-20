import os
import html
import pandas as pd
import folium

# 1. Configuración de rutas
# Leemos desde la carpeta 'data/espaciosTotales.csv'
CSV_PATH = os.path.join('data', 'espaciosTotales.csv')
OUTPUT_MAP = 'mapaCultural.html'

def generar_mapa():
    # 2. Leer el CSV
    if not os.path.exists(CSV_PATH):
        # Fallback por si acaso está en el directorio raíz
        if os.path.exists('espaciosTotales.csv'):
            path_to_read = 'espaciosTotales.csv'
        else:
            print(f"Error: No se pudo encontrar el archivo {CSV_PATH}")
            return
    else:
        path_to_read = CSV_PATH

    print(f"Cargando datos desde {path_to_read}...")
    df = pd.read_csv(path_to_read)
    
    # 3. Crear el mapa de Folium centrado en las coordenadas de Argentina
    # Latitud: -38.4161, Longitud: -63.6167
    print("Inicializando mapa de Folium...")
    mapa = folium.Map(location=[-38.4161, -63.6167], zoom_start=5)
    
    # 4. Definir diccionario de colores para las categorías
    colores_categoria = {
        'Biblioteca Popular': 'blue',
        'Salas de Teatro': 'red',
        'Espacios de Exhibición Patrimonial': 'green',
        'Centro Cultural': 'purple',
        'Salas de cine': 'orange'
    }
    
    # 5. Iterar sobre las filas y agregar CircleMarker por cada espacio cultural
    print("Agregando marcadores al mapa...")
    for idx, row in df.iterrows():
        lat = row['latitud']
        lon = row['longitud']
        
        # Omitir si las coordenadas no son válidas por alguna razón
        if pd.isna(lat) or pd.isna(lon):
            continue
            
        # Determinar el color según la categoría
        cat = row['categoria']
        color = colores_categoria.get(cat, 'gray')
        
        # 6. Escapar los textos en HTML básico para el Popup de forma segura
        nombre_esc = html.escape(str(row['nombre']))
        categoria_esc = html.escape(str(row['categoria']))
        provincia_esc = html.escape(str(row['provincia']))
        localidad_esc = html.escape(str(row['localidad']))
        direccion_esc = html.escape(str(row['direccion']))
        
        # 7. Formato HTML para el Popup
        popup_content = f"""
        <div style="font-family: Arial, sans-serif; font-size: 12px; line-height: 1.4; min-width: 150px;">
            <strong>{nombre_esc}</strong><br>
            <strong>Categoría:</strong> {categoria_esc}<br>
            <strong>Provincia:</strong> {provincia_esc}<br>
            <strong>Localidad:</strong> {localidad_esc}<br>
            <strong>Dirección:</strong> {direccion_esc}
        </div>
        """
        
        # Crear marcador circular
        folium.CircleMarker(
            location=[lat, lon],
            radius=8,
            color=color,
            fill_color=color,
            fill_opacity=0.7,
            popup=folium.Popup(popup_content, max_width=300)
        ).add_to(mapa)
        
    # 8. Guardar el mapa en mapa_cultural.html
    print(f"Guardando mapa interactivo en {OUTPUT_MAP}...")
    mapa.save(OUTPUT_MAP)
    print("Mapa interactivo generado con éxito.")

if __name__ == "__main__":
    generar_mapa()
