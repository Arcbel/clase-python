#Escriba un programa que eliminae un signo de exclamación del final de una cadena. 
#    puede suponer que los datos de entrada son siempre una cadena, no es necesario verificarlos.

cadena = input("Ingrese un texto que termine con signo de exclamación:")

if cadena[-1]:
    nueva_cadena = cadena[:-1]
    print("El nuevo texto es: " + nueva_cadena)
else:
    print("El texto ingresado no termina con signo de exclamaxión")