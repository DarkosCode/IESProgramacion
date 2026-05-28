from schema.paciente import Paciente
import pandas

df_excel = pandas.read_excel("data/pacientes.xlsx", sheet_name="Hoja1")

df_excel = df_excel.rename(columns={"altura": Paciente.COL_ESTATURA,
                                    "peso":Paciente.COL_PESO,
                                    "temperatura": Paciente.COL_TEMPERATURA})

df_excel[Paciente.COL_TENSION_ARTERIAL] = df_excel["presion sistólica"].astype(str) + "/" + df_excel["presión diastólica"].astype(str)
df_excel = df_excel.drop(columns=["presion sistólica", "presión diastólica"])

df_excel[Paciente.COL_INGRESO] = df_excel["fecha"].astype(str) + " " + df_excel["hora"].astype(str)
df_excel = df_excel.drop(columns=["fecha", "hora"])

df_excel.columns = df_excel.columns.map(lambda c: c if c[0].isupper() else c.capitalize())

df_excel[Paciente.COL_PACIENTE] = df_excel[Paciente.COL_PACIENTE].map(lambda p: f"{str(p).split(" ")[1].upper()}, {str(p).split(" ")[0]}")