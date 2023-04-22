#Diccionario: orden en las claves - son mutables - claves deben ser únicas -son de rápido ecceso
empty_dict = {} #diccionario vacio

fulfilled_dict= {
    "id": 1,
    "name": "Valeria"
}
print (empty_dict)
print (fulfilled_dict)

lista_1 = ["a1", "b2"]
dict_converted = dict(lista_1)
print(lista_1, dict_converted)

tupla_1 = ("a1", "b2")
print(tupla_1, dict(tupla_1))

lista_dimensional = [["a", 1], ["b", 2]]
print(lista_dimensional, dict(lista_dimensional))

dict_1 = {
    "iden": 1,
    "nombre": "Valeria"
}
print(dict_1["nombre"]) #obtener un elemento del dict

dict_1["edad"] = 29 #agregar un elemento
print(dict_1)

dict_1["iden"] = 4 #cambiar un elemento
print(dict_1)

del dict_1["nombre"] #eliminar elemento
print(dict_1)

empty_dict_2 = dict() #crea dict vacio
print(empty_dict_2)

full_dict = dict(
    genero = "F",
    nacionalidad = "Chilena"
)

print(full_dict)

empleado = {
    "nombre": "Valeria",
    "apellido": "Rojas",
    "edad": 29,
    "rut": "18.590.124-0"
}
print (empleado)

for variablex in empleado.values(): #se usa para recorrer los elementos del dict por sus valores
    print(variablex)

print (empleado)

for a, b in empleado.items(): #recorre la clave y valor
    print(a, b)

#Condicionales: if + condicion: bloque de codigo

edad = 60
if edad > 50: #despues de esto tiene que estar identado para que sea parte del if
    print ("Hola Don")
    print ("Hola desde dentro del if")

print("se imprime no importa lo que pase")

temp = 36
if temp >= 37:
    print("temperatura alta")
elif temp < 35: #con el elif cuando se cumple deja de evaluar
    print("temperatura baja")
else:
    print("temperatura normal")

temperatura = 5
pais = "Chile"

if temperatura <10:
    if pais == "Chile":
        print("ccc")
    else:
        print("zzzz")

##Ejercicio: Escriba una programa que permita adivinar un personaje de marvel
##en base a estas 3 preguntas
##1 puede volar?
##2 es humano?
##3 tiene mascara?

vuela = input("¿Puede volar?:")
humano = input("¿Es humano?:")
mascara = input("¿Tiene máscara?:")

if vuela == "si":
    if humano == "si":
        if mascara == "si":
            print("es Iron Man")

elif vuela == "si":
    if humano == "no":
        if mascara == "no":                ##ASI NO ES! CORRIGELO VALERIA 
            print("es Thor")

elif vuela == "si":
    if humano == "si":
        if mascara == "no":
            print("es Dr Strange")

else:
    print("vuelva a responder")



##CICLOS
##WHILE 1

want_exit = "n"
while want_exit == "n":
    print("hola, como estas")
    want_exit = input("quieres salir S/N??")

print("fuera del while")

##While 2

want_exit = "n"
num_questions = 0
while want_exit == "n":
    print("hola, como estas")
    want_exit = input("quieres salir S/N??")
    num_questions += 1
    if num_questions == 4:
        print ("alcanzaste el nmax permitido")
        break
print("fuera del while")
