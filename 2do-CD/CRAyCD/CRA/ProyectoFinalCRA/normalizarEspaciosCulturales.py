import os
import pandas as pd
import numpy as np

# Configuración de directorios y nombres de archivos
DATA_DIR = os.path.join('data', 'datosCrudos')
OUTPUT_FILE = os.path.join('data', 'espaciosTotales.csv')

# Mapeo de columnas originales a los nombres estandarizados requeridos:
# 'id_provincia', 'provincia', 'localidad', 'nombre', 'direccion', 'latitud', 'longitud', 'categoria'
FILE_MAPPINGS = {
    'bibliotecasPopulares.csv': {
        'id_provincia': 'id_provincia',
        'provincia': 'provincia',
        'localidad': 'localidad',
        'nombre': 'nombre',
        'domicilio': 'direccion',
        'latitud': 'latitud',
        'longitud': 'longitud',
        'categoria': 'categoria'
    },
    'centrosCulturales.csv': {
        'ID_PROV': 'id_provincia',
        'Provincia': 'provincia',
        'Localidad': 'localidad',
        'Nombre': 'nombre',
        'Domicilio': 'direccion',
        'Latitud': 'latitud',
        'Longitud': 'longitud',
        'Categoria': 'categoria'
    },
    'museos.csv': {
        'IdProvincia': 'id_provincia',
        'provincia': 'provincia',
        'localidad': 'localidad',
        'nombre': 'nombre',
        'direccion': 'direccion',
        'Latitud': 'latitud',
        'Longitud': 'longitud',
        'categoria': 'categoria'
    },
    'salasCines.csv': {
        'id_provincia': 'id_provincia',
        'provincia': 'provincia',
        'localidad': 'localidad',
        'nombre': 'nombre',
        'direccion': 'direccion',
        'latitud': 'latitud',
        'longitud': 'longitud',
        'categoria': 'categoria'
    },
    'teatros.csv': {
        'id_prov': 'id_provincia',
        'provincia': 'provincia',
        'localidad': 'localidad',
        'nombre': 'nombre',
        'domicilio': 'direccion',
        'latitud': 'latitud',
        'longitud': 'longitud',
        'categoria': 'categoria'
    }
}

def run_etl():
    dataframes = []
    
    print("Iniciando proceso de ETL...")
    
    # 1. Leer los 5 archivos CSV desde la carpeta "data"
    for filename, col_map in FILE_MAPPINGS.items():
        file_path = os.path.join(DATA_DIR, filename)
        if not os.path.exists(file_path):
            print(f"Error: El archivo {file_path} no existe.")
            continue
            
        print(f"Procesando: {filename}...")
        
        # Leemos el archivo. Probamos con UTF-8.
        try:
            # Dado que algunos CSVs pueden usar diferentes codificaciones,
            # intentamos leer con utf-8 y si falla con latin-1.
            try:
                df = pd.read_csv(file_path, encoding='utf-8')
            except UnicodeDecodeError:
                df = pd.read_csv(file_path, encoding='latin-1')
            
            # 2. Extraer de cada uno estrictamente las columnas referentes a: ID de provincia, Provincia, 
            # Localidad, Nombre, Domicilio/Dirección, Latitud, Longitud y Categoría.
            # Verificamos que las columnas existan en el DataFrame antes de filtrarlas
            missing_cols = [col for col in col_map.keys() if col not in df.columns]
            if missing_cols:
                print(f"  Advertencia: Faltan columnas en {filename}: {missing_cols}")
                # Si falta alguna columna, intentaremos buscar una coincidencia insensible a mayúsculas/minúsculas
                # para hacer el script aún más robusto.
                actualized_map = {}
                for orig_col, target_col in col_map.items():
                    if orig_col in df.columns:
                        actualized_map[orig_col] = target_col
                    else:
                        # Búsqueda insensible
                        found = False
                        for col in df.columns:
                            if col.lower() == orig_col.lower():
                                actualized_map[col] = target_col
                                found = True
                                break
                        if not found:
                            print(f"  No se encontró equivalente para la columna: {orig_col}")
                col_map = actualized_map
            
            # Filtramos por las columnas existentes en el mapeo
            df_filtered = df[list(col_map.keys())].copy()
            
            # 3. Estandarizar los nombres de estas columnas
            df_filtered.rename(columns=col_map, inplace=True)
            
            # Agregamos al listado de DataFrames
            dataframes.append(df_filtered)
            print(f"  -> Cargadas {df_filtered.shape[0]} filas.")
            
        except Exception as e:
            print(f"Error al leer/procesar {filename}: {e}")
            
    if not dataframes:
        print("No se cargaron DataFrames. Saliendo.")
        return
        
    # 4. Concatene los 5 dataframes en uno solo maestro
    print("Concatenando DataFrames...")
    df_maestro = pd.concat(dataframes, ignore_index=True)
    print(f"DataFrame unificado: {df_maestro.shape[0]} filas totales antes de la limpieza.")
    
    # 5. Realice la siguiente limpieza en el dataframe unificado:
    # A. Reemplaza los textos "s/d" por valores nulos reales (NaN) (sin importar mayúsculas/minúsculas)
    print("Reemplazando valores 's/d' por NaN...")
    # Reemplazamos s/d en cualquier columna
    df_maestro = df_maestro.replace(to_replace=r'(?i)^\s*s/d\s*$', value=np.nan, regex=True)
    
    # B. Estandarizar nombres de provincias (limpiar espacios en blanco y unificar nombres con/sin acento)
    print("Estandarizando nombres de provincias...")
    if 'provincia' in df_maestro.columns:
        # Eliminar espacios en blanco alrededor (incluyendo caracteres unicode como \xa0)
        df_maestro['provincia'] = df_maestro['provincia'].astype(str).str.strip()
        
        # Mapeo para corregir acentos y nombres duplicados
        provincia_mapeo = {
            'Ciudad Autonoma de Buenos Aires': 'Ciudad Autónoma de Buenos Aires',
            'Cordoba': 'Córdoba',
            'Entre Rios': 'Entre Ríos',
            'Neuquen': 'Neuquén',
            'Rio Negro': 'Río Negro',
            'Tucuman': 'Tucumán',
            'Tierra del Fuego': 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'
        }
        df_maestro['provincia'] = df_maestro['provincia'].replace(provincia_mapeo)
    
    # C. Asegúrate de que las columnas 'latitud' y 'longitud' sean de tipo numérico (float) forzando los errores a NaN
    print("Convirtiendo 'latitud' y 'longitud' a numérico...")
    df_maestro['latitud'] = pd.to_numeric(df_maestro['latitud'], errors='coerce')
    df_maestro['longitud'] = pd.to_numeric(df_maestro['longitud'], errors='coerce')
    
    # D. Elimina cualquier fila que no tenga coordenadas válidas (nulos en 'latitud' o 'longitud')
    print("Eliminando filas sin coordenadas válidas...")
    filas_antes = df_maestro.shape[0]
    df_maestro.dropna(subset=['latitud', 'longitud'], how='any', inplace=True)
    filas_despues = df_maestro.shape[0]
    print(f"  -> Se eliminaron {filas_antes - filas_despues} filas sin coordenadas válidas.")
    print(f"  -> Quedan {filas_despues} filas en el DataFrame final.")
    
    # 6. Exporte el dataframe resultante como un nuevo archivo llamado "espaciosCulturalesLimpio.csv" 
    # en el directorio actual (fuera de la carpeta data), sin incluir el índice.
    print(f"Exportando a {OUTPUT_FILE}...")
    df_maestro.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
    print("Proceso finalizado con éxito.")

if __name__ == "__main__":
    run_etl()
