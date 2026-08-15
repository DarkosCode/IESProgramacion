import numpy as np, statistics
from scipy import stats

# rango = np.arange(1, 7)
# print(rango)

edades = np.random.default_rng().integers(low=18, high=81, size=100)
#* El parametro default_rng(seed=42) fija los valores aleatorios y deja de ser "aleatorio"
# print("Muestra: ", edades)

promedio = np.mean(edades)
print("Promedio: ", promedio, "\n")
mediana = np.median(edades)
print("Mediana: ", mediana, "\n")
desvEstd = round(np.std(edades), 3)
print("Desviacion estandar: ", desvEstd, "\n")
varianza = round(np.var(edades), 3)
print("Varianza/Dispersion: ", varianza, "\n")

#! SCIPY

moda = stats.mode(edades, keepdims=True)
# True si queremos una distribucion de solo una moda.
print("Moda: ", moda.mode[0], "\n")

# moda1 = stats.mode(edades, keepdims=False).mode
# print("Moda1: ", moda1.mode[0], "\n")

modas = statistics.multimode(edades)
modas = [int(m) for m in modas]
print("Modas: ", modas)
#* Esto calcula/muestra las distintas modas (si es que hay), es decir:
#* si hay dos numeros en el array que se repiten por ejemplo 8 veces y son los que mas se repiten.

# coeficiente_fisher = 