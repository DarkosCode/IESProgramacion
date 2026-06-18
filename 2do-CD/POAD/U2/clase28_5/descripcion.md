Este proyecto es una aplicación de análisis y visualización de datos de
pacientes. Está diseñado siguiendo una arquitectura modular que separa la
extracción de datos, el procesamiento, la definición de esquemas y la
visualización.

A continuación, te detallo la estructura y el propósito de cada archivo:

📂 Estructura del Proyecto

1. Archivos Principales (Raíz)

- main.py: Es el punto de entrada de la aplicación. Se encarga de
  coordinar todo el flujo: importa los datos ya procesados, utiliza las
  constantes del esquema y llama a las funciones de visualización para
  generar los gráficos.
- data_processing.py: Actúa como el motor de limpieza y consolidación.
  Importa los datos desde las distintas fuentes (JSON y Excel), los une
  en un solo DataFrame, elimina registros duplicados y prepara la
  versión final de los datos para ser analizados.

2. Carpeta schema/ (Definición de Datos)

- paciente.py: Contiene la clase Paciente, que define constantes para
  los nombres de las columnas (ej. COL_EDAD, COL_SEXO). Esto es una
  buena práctica porque centraliza el "nombre de los campos", evitando
  errores de escritura en el resto del código y facilitando cambios
  futuros.

3. Carpeta sources/ (Adaptadores de Datos)
   Esta carpeta se encarga de la Normalización. Cada archivo lee un formato
   distinto y lo adapta al esquema común:

- pacientes_json.py: Lee el archivo pacientes.json, renombra sus
  columnas, normaliza el género (ej: "F" a "mujer"), convierte unidades
  (estatura de cm a metros) y formatea los nombres de los pacientes.
- pacientes_xlsx.py: Lee el archivo pacientes.xlsx. Realiza
  transformaciones más complejas, como combinar la presión sistólica y
  diastólica en un solo campo o unir fecha y hora en una columna de
  ingreso.

4. Carpeta view/ (Capa de Visualización)
   Contiene utilitarios para generar gráficos utilizando diferentes
   librerías:

- matplotlib_utils.py: Genera una Pirámide Poblacional (comparativa de
  edades entre hombres y mujeres) usando Matplotlib.
- plotly_utils.py: Crea un Histograma interactivo de edades utilizando
  Plotly.
- seaborn_utils.py: Genera un Mapa de Calor (Heatmap) de correlación
  entre las variables numéricas usando Seaborn.

5. Carpeta data/

- Contiene los archivos de datos crudos: pacientes.json y
  pacientes.xlsx.

⚙️ ¿Cómo funciona el flujo de trabajo?

1.  Al ejecutar main.py, este solicita los datos a data_processing.py.
2.  data_processing.py a su vez solicita los datos a los archivos en
    sources/.
3.  Los scripts en sources/ leen los archivos de la carpeta data/, los
    "limpian" para que todos tengan el mismo formato (basándose en
    schema/paciente.py) y se los devuelven a data_processing.
4.  Una vez que los datos están unificados y limpios en un solo lugar,
    main.py los envía a las funciones de la carpeta view/.
5.  Finalmente, se abren tres ventanas o pestañas de navegador mostrando
    los análisis visuales de los pacientes.
