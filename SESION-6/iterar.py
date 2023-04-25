words = "Esto es una cadena de texto"

word = ""
for letter in words:
    print(letter)


for letter in words:
    if letter != " ":
        word += letter
    else:
        print(word)
        word = ""

print("\n----------------")
for letter in words:
    if letter != " ":
        print(letter)
    else:
        break

print("\n----------------")
animal_list = ["Gato", "Perro", "Pajaro", "Leon"]
for animal in animal_list:
    print(animal)

print("\n----------------")

list1 = range(2,3)
print(list1)

for number_in in range(1, 10): #de 1 en 1
    print(number_in)

for number_in in range(1, 10, 2): #de 2 en 2
    print(number_in)

for number_in in range(1, 10, 3): #de 3 en 3
    print(number_in)

print("\n------------Tablas de multiplicar------------\n")

for num_tabla in range (1, 11):
    for num_mult in range (1, 11):
        result = num_tabla * num_mult
        print (f'{num_tabla} x {num_mult} = {result}')
    print("\n---------------\n")

print("\n------------Arreglos bidimensionales------------\n")

double_list = [[1, 2, 3], [4, 5, 6]]

print(double_list[0])
print(double_list[1])

print(double_list[0][2])
print(double_list[1][2])

