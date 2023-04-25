#Dado un mes como un número entero del 1 al 12, devuelva a qué trimestre del año pertenece como un número entero.
#    Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio), 
#    forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.

mes = int(input("Escriba el mes en número (del 1 al 12):")) ## int() convierte el valor ingresado en un num entero, no una cadena de texto

if mes >= 1 and mes <= 3:
    print ("Este mes corresponde al primer trimestre")
elif mes >= 4 and mes <= 6:
    print ("Este mes corresponde al segundo trimestre")
elif mes >= 7 and mes <= 9:
    print ("Este mes corresponde al tercer trimestre")
elif mes >= 10 and mes <= 12:
    print ("Este mes corresponde al cuarto trimestre")
else:
    print("Por favor ingrese un numero entero del 1 al 12 que corresponda al mes")