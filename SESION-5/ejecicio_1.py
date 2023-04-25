#1. Cree un programa que encuentre el promedio de los tres puntajes dados y devuelva el valor de la letra 
#asociada con esa calificación. con la siguiente tabla
#    0   - 2     D
#    2.1 - 5     C
#    5.1 - 6     B
#    6.1 - 7     A

nota = input("Escribe aquí tu nota(del 0 al 7):")

if nota >= "0" and nota <= "2":
    print ("Tu calificación es D")
elif nota >= "2.1" and nota <= "5":
    print ("Tu calificacion es C")
elif nota >= "5.1" and nota <= "6":
    print ("Tu calificacion es B")
elif nota >= "6.1" and nota <= "7":
    print ("Tu calificacion es A")
else:
    print("Por favor ingrese una nota del 0 al 7 (decimales separados por puntos)")