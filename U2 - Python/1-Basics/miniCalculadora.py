
## !
numeroUno = input('Ingresa el primer numero ')
while True:
    operador = input('Ingresa el operador ')
    if operador in ['+', '-', '*', '/', '%']:
        break
    else:
        print('El operador debe ser uno de los siguientes: +, -, *, /, %')
numeroDos = input('Ingresa el segundo numero ')

operacion = numeroUno + operador + numeroDos
print(f'La operacion {operacion} da como resultado: {eval(operacion)}')
