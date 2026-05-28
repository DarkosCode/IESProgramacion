import pandas
from sources.pacientes_json import df_json
from sources.pacientes_xlsx import df_excel

df = pandas.concat([df_excel, df_json])

df = df.drop_duplicates()

df_personas = df.drop_duplicates(["Paciente"])