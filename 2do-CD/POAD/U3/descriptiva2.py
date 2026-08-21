import numpy, pandas
import plotly.figure_factory as ff
from scipy.stats import norm

SEMILLA = 42

print("Otra vez edades.")

N_p = 10000
poblacion = numpy.random.default_rng(seed=SEMILLA).integers(18, 81, size=N_p)
print("Tamaño de población:", N_p)

desviacion = numpy.std(poblacion, ddof=1)
print("Desviación estándar:", desviacion)

err = 0.05 * desviacion
print("Error deseado:", err)

confianza = 0.9973 # 0.6827, 0.9545, 0.9973
z = norm.ppf((1 - confianza)/2)
print("Valor crítico:", z)

varianza = numpy.var(poblacion, ddof=1)
print("Varianza:", varianza)

# Fórmula de Cochran para variable cuantitativa continua de población finita.
# Usar 0.25 en vez de varianza para variable cualitativa de población finita.
n0_m = pow(z, 2) * varianza / pow(err, 2)
n0_m = n0_m / (1 + (n0_m - 1) / N_p)
n0_m = int(numpy.ceil(n0_m))
print("Tamaño de muestra significativa no representativa:", n0_m)

n_m = (N_p * pow(z, 2) * varianza) \
    / ((N_p - 1) * pow(err, 2) + pow(z, 2) * varianza)
n_m = int(numpy.ceil(n_m))
print("Tamaño de muestra significativa y representativa:", n_m)

indices_muestra = numpy.random.default_rng(seed=SEMILLA).choice(len(poblacion), size=n_m, replace=False)
muestra = poblacion[indices_muestra]
print("Muestra:", muestra)

k = int(1 + numpy.log2(n_m))
print("Regla de Sturges:", k)

frecuencias, bins = numpy.histogram(muestra, bins=k)
frecuencia_relativa = frecuencias / n_m
frecuencia_acumulada = numpy.cumsum(frecuencias)
frecuencia_relativa_acumulada = numpy.cumsum(frecuencia_relativa)

tabla = pandas.DataFrame({
    "Intervalo": [f"{int(bins[i])}-{int(bins[i+1]-1)}" for i in range(len(bins)-1)],
    "Frecuencia absoluta": frecuencias,
    "Frecuencia relativa": numpy.round(frecuencia_relativa, 3),
    "Frecuencia acumulada": frecuencia_acumulada,
    "Frecuencia relativa acumulada": numpy.round(frecuencia_relativa_acumulada, 3)
})

fig = ff.create_table(tabla)
fig.show()