# Proyecto de Unificación y Visualización Geográfica de Espacios Culturales

Este proyecto realiza un proceso completo de ETL (Extracción, Transformación y Carga) para consolidar y estandarizar datos de diversos espacios culturales en Argentina (bibliotecas populares, museos, salas de teatro, cines y centros culturales) y visualizarlos en un mapa interactivo.

## Estructura del Proyecto

* **`data/datosCrudos/`**: Carpeta que almacena los 5 conjuntos de datos originales en formato CSV.
* **`data/espaciosTotales.csv`**: El dataset maestro resultante tras la limpieza y unificación de datos.
* **`normalizarEspaciosCulturales.py`**: Script de ETL que limpia y consolida los archivos de entrada.
* **`generarMapa.py`**: Script que genera la visualización en mapa web interactivo.
* **`mapaCultural.html`**: El mapa interactivo resultante donde se visualizan todos los puntos.
* **`readme.md`**: Este archivo de documentación del proyecto.

## Funcionalidad de los Scripts

### 1. ETL y Limpieza (`normalizarEspaciosCulturales.py`)
Este script unifica la estructura de los CSVs originales realizando las siguientes tareas:
* Filtra solo las columnas necesarias (`id_provincia`, `provincia`, `localidad`, `nombre`, `direccion`, `latitud`, `longitud`, `categoria`).
* Estandariza la codificación de caracteres a UTF-8/Latin-1.
* Limpia los valores `"s/d"` (sin datos) reemplazándolos por nulos reales (`NaN`).
* Limpia y unifica los nombres de las provincias (corrigiendo faltas de tildes y duplicados de nombres).
* Convierte las coordenadas a flotantes y elimina los registros con coordenadas inválidas o nulas.
* Une los dataframes en un dataset único consolidado.

### 2. Generación del Mapa (`generarMapa.py`)
Toma el dataset unificado y crea una representación espacial:
* Centra el mapa interactivo en la República Argentina.
* Categoriza cada tipo de espacio cultural utilizando colores diferenciados:
  * **Bibliotecas Populares**: Azul
  * **Teatros**: Rojo
  * **Museos**: Verde
  * **Centros Culturales**: Púrpura
  * **Salas de Cine**: Naranja
* Añade marcadores circulares de tamaño visible (`radius=8`) y opacidad suave (`0.7`) para facilitar la navegación a gran escala.
* Cada marcador incluye un popup interactivo con la información formateada del espacio.

---

## Requisitos de Ejecución

Para poder ejecutar los scripts en tu entorno local, asegúrate de contar con los siguientes prerrequisitos:

### Versión de Python
* **Python 3.8 o superior** (Desarrollado y probado con Python 3.12).

### Librerías Requeridas
Las dependencias necesarias son **Pandas** y **Folium**. Puedes instalarlas ejecutando:

```bash
pip install pandas folium
```

### Instrucciones de Uso

1. Coloca los archivos CSV crudos dentro de `data/datosCrudos/`.
2. Ejecuta el script de ETL para procesar y limpiar los datos:
   ```bash
   python normalizarEspaciosCulturales.py
   ```
3. Ejecuta el script de mapa para generar la visualización:
   ```bash
   python generarMapa.py
   ```
4. Abre el archivo resultante `mapaCultural.html` en cualquier navegador web para explorar el mapa interactivo.
