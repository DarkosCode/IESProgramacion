import matplotlib.pyplot as plt

#? Primeros ejercicios con librerias de MatPlotLiB

#*1.1 Basicas
ejeX = [1, 2, 3, 4]
ejeY = [10, 20, 30, 40]

plt.plot(ejeX, ejeY)
plt.title("Primer Grafico")
plt.show()

#*Etiquetando Ejes
plt.xlabel("Horizontal!")
plt.ylabel("Vertical!")