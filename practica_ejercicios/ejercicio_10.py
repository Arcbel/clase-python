edad_minima = 16
ingreso_minimo = 1000

edad = int(input('Ingrese su edad: '))
ingreso = int(input('Ingrese su ingreso mensual: '))

if edad > edad_minima:
    if ingreso >= ingreso_minimo:
        print('Debe tributar')
    else:
        print('No debe tributar')
else:
    print('No debe tributar')