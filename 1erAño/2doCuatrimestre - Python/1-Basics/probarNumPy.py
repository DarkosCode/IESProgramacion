import numpy as np

# Crear una matriz 2x3
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
"""""

# Acceder a un elemento (fila 1, columna 2)
print(matriz[0, 1])  # Salida: 2

# Modificar un elemento
matriz[1, 2] = 9
print(matriz)  # Salida: [[1 2 3] [4 5 9]]

# Operaciones matemáticas
matriz2 = np.array([[1, 1, 1], [1, 1, 1]])
suma = matriz + matriz2
print(suma)  # Salida: [[2 3 4] [5 6 10]]
"""""

