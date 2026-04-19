import numpy as np

array = np.arange(1, 11)
print(".arrange", array, "\n")

mayores_a_5 = array[array > 5]
print("mayores a 5:", mayores_a_5, "\n")

ceros = np.zeros((3, 4))
print(".zeros", ceros, "\n")

#* Matriz identidad
identidad = np.eye(4)
print(".eye", identidad, "\n")

#* Multiplicacion matrices
matriz1 = np.array([[1, 2], [3, 4]])
print("matriz1", "\n", matriz1, "\n")

matriz2 = np.array([[5, 6], [7, 8]])
print("matriz2", "\n", matriz2, "\n")

producto = np.dot(matriz1, matriz2)
print("producto de matrices", "\n", producto, "\n")