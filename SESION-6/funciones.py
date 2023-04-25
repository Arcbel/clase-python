###Funciones: Extractos de código que se repiten

def saludar (name):
    print(f'Hola {name}')

def saludar_dos(first_name, last_name):
    print(f'Hola {first_name}, {last_name}!!')

def multiplicar_texto(texto, multiplier = 2):
    print(texto * multiplier)

saludar('Rodrigo')
saludar('Richar')

saludar_dos (last_name = 'Lujano', first_name= 'Richar')

multiplicar_texto("V", 5)

multiplicar_texto("X")

def varieltal(param1, param2, *others): #el * forma tuplas
    print(param1)
    print(param2)
    print(others)

varieltal("A1", "2B", "0", "XX")

def varieltal_dos(param1, **others): #el * forma tuplas
    print(param1)
    print(others)

varieltal_dos("A1", id = 0, name = "Carlos", age = 22)