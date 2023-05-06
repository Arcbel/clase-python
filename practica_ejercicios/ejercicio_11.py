nombre = input('Ingrese su nombre: ').lower()
sexo = input('Ingrese su sexo (mujer o hombre): ').lower()

primera_letra = nombre[0]

if sexo == 'mujer':
    if primera_letra < 'm':
        print('Pertenece al grupo A')
    else:
        print('Pertenece al grupo B')
elif sexo == 'hombre':
    if primera_letra > 'n':
        print('Pertenece al grupo A')
    else:
        print('Pertenece al grupo B')

