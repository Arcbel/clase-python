#2. utilizando dos while anidados, construya la tablas de mutiplicacion, ejemplo
#    Ejemplo whiole anidados:
#    while codicion1
#        while codicion2
#            .....

a = 1
while a <= 10:
    b = 1
    while b <= 10:
        resultado = a * b
        print(f"{a} x {b} = {resultado}")  ## f-string: se utilizan para insertar valores de variables en una cadena de texto.
        b += 1
    a += 1