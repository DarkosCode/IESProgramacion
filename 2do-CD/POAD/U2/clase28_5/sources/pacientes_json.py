from schema.paciente import Paciente
import pandas

df_json = pandas.read_json("data/pacientes.json")

df_json = df_json.rename(columns={"Nombre": Paciente.COL_PACIENTE,
                          "Estatura": Paciente.COL_ESTATURA,
                          "Peso": Paciente.COL_PESO,
                          "Temperatura": Paciente.COL_TEMPERATURA,
                          "Presión": Paciente.COL_TENSION_ARTERIAL})

df_json[Paciente.COL_SEXO] = df_json[Paciente.COL_SEXO].replace({"F": "mujer", "M": "hombre"})

df_json[Paciente.COL_PACIENTE] = df_json[Paciente.COL_PACIENTE].map(lambda p: f"{str(p).split(" ")[1].upper()}, {str(p).split(" ")[0]}")

df_json[Paciente.COL_ESTATURA] = df_json[Paciente.COL_ESTATURA] / 100