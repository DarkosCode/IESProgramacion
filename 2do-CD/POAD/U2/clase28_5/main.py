from data_processing import df, df_personas
from schema.paciente import Paciente
from view.matplotlib_utils import piramide_poblacional
from view.seaborn_utils import mapa_calor
from view.plotly_utils import histograma

# pip install pandas matplotlib seaborn plotly openpyxl

def main():
    hombres = df_personas[df_personas[Paciente.COL_SEXO] == "hombre"][Paciente.COL_EDAD]
    mujeres = df_personas[df_personas[Paciente.COL_SEXO] == "mujer"][Paciente.COL_EDAD]
    piramide_poblacional(hombres, mujeres)
    mapa_calor(df)
    histograma(df_personas[Paciente.COL_EDAD])

if __name__ == "__main__":
    main()