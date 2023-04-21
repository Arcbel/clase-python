print("======String======")
#Concatenar
first_name = "Valeria"
last_name = "Rojas"
print(first_name + " " + last_name)

age = "29"
gender = "Femenino"
print(age + ", " + gender)

#Multiplicar
mensaje1 = "Hola " * 3
print(mensaje1)

#Añadir
mensaje3 = "Sebastian"
print(mensaje3)
mensaje3 += ","
print(mensaje3)
mensaje3 += " Rojas"
print(mensaje3)

#Funcion[built-in] len -> obtener total de caracteres
print(len(mensaje3))

#Funcion[own] find -> busca la conincidencia dentro de un string
cadena = "esto es una oracion por ucrania"
posicion = cadena.find("pelo")
print("pelo se encuentra en: ", posicion)
posicion = cadena.find("ucrania")
print("pelo se encuentra en: ", posicion)

#lower() convierte texto a minusculas
cadena2 = "CALLEJON- almagro"
cadena2_lower = cadena2.lower()
print(cadena2)
print(cadena2_lower)

#replace() reemplaza string
print(cadena2.replace( "-", ":"))

print("======Listas======") #MUTABLES

empty_list = []
print(empty_list)

fullfiled_list = [1, 3, 500, 1.4, [2, "a"], {"name": "Richar"}, (1,3,5)]
print(fullfiled_list)

second_list= list()
print(second_list)

print(list("concurso"))

range_one = range(10)
print(list(range_one))

numeros = [1,4,6]
numeros.append(10)
print(numeros)

print(numeros[2])

for y in numeros:
    print (y)

numeros.remove(6) #lista.pop(posicion) del lista[posicion]
print(numeros)

numeros[1] = 50
print(numeros)

print("=====Tuplas=====") #INMUTABLES

empty_tupla = ()
fullfiled_tupla = (1, "Richar", 3.4)
print(empty_tupla, fullfiled_tupla )

print(type(fullfiled_tupla))

one_tupla = ("juan",)
print (type(one_tupla))

hojas = "carta", "oficio" #lo toma como tupla pero se escribir entre parentesis
print(type(hojas))
print(hojas)

list_to_convert = [2, 6, 8, 9]
print(list_to_convert)

tuple_converted = tuple(list_to_convert) #para convertir una lista en tupla
print(tuple_converted)

tupla = (1, 2 , 3 , 4)
tupla = tupla[::-1]
print(tupla)



