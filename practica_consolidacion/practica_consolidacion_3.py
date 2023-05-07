magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = ['Messi', 'Pele', 'Juanes']

def hacer_grandioso(lista_magos):
    for i in range(len(lista_magos)):
        lista_magos[i] = "El gran " + lista_magos[i]

def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

print("Lista completa de nombres:")
imprimir_nombres(magos + cientificos + otros)

hacer_grandioso(magos)
print("\nMagos grandiosos:")
imprimir_nombres(magos)

print("\nCientíficos:")
imprimir_nombres(cientificos)

print("\nOtros:")
imprimir_nombres(otros)