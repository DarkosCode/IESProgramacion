import matplotlib.pyplot as plt
import numpy, statistics
from scipy import stats
import seaborn

edades = numpy.random.default_rng(seed=42).integers(18, 81, size=100)
print("Muestra:", edades)

media = numpy.mean(edades)
print("Media:", media)

mediana = numpy.median(edades)
print("Mediana:", mediana)

moda_unica = stats.mode(edades, keepdims=True)
print("Moda única:", moda_unica.mode[0], "con frecuencia", moda_unica.count[0])

modas_multiples = statistics.multimode(edades)
modas_multiples = [int(m) for m in modas_multiples]
print("Múltiples modas:", modas_multiples)

desviacion = numpy.std(edades, ddof=1)
print("Desviación estándar:", desviacion)

varianza = numpy.var(edades, ddof=1)
print("Varianza:", varianza)

asimetria_fisher = stats.skew(edades)
print("Coeficiente de Fisher (asimetría):", asimetria_fisher)
if asimetria_fisher > 0:
    print("Sesgo derecho.")
elif asimetria_fisher < 0:
    print("Sesgo izquierdo.")
else:
    print("Distribución simétrica.")

curtosis = stats.kurtosis(edades, fisher=False)
print("Curtosis:", curtosis)
if curtosis > 3:
    print("Distribución leptocúrtica.")
elif curtosis < 3:
    print("Distribución platicúrtica.")
else:
    print("Distribución mesocúrtica.")

seaborn.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
seaborn.histplot(edades, kde=True, stat="density", color="teal", bins=15)

plt.title('Distribución de Edades (Seaborn)')
plt.xlabel('Edad')
plt.ylabel('Densidad')
plt.show()