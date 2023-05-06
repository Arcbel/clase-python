dividendo = int(input('Ingrese un dividendo: '))
divisor = int(input('Ingrese un divisor: '))

if divisor == 0:
    print('No se puede dividir por cero')
else:
    resultado = dividendo / divisor
    print(f'El resultado es {resultado}')