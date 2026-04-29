# Datos de la flota
x = [320, 150, 480, 210, 95, 560, 340, 420, 180, 275]  # kilómetros
y = [28, 14, 39, 20, 11, 44, 30, 37, 17, 25]            # litros

# Promedios
x_media = sum(x) / len(x)
y_media = sum(y) / len(y)

# Numerador y denominador de B1
numerador = sum((x[i] - x_media) * (y[i] - y_media) for i in range(len(x)))
denominador = sum((x[i] - x_media) ** 2 for i in range(len(x)))

# Cálculo de B1 y B0
b1 = numerador / denominador
b0 = y_media - b1 * x_media

print(f"B1 = {b1:.4f}")
print(f"B0 = {b0:.4f}")