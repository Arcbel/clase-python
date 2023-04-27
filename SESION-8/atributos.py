
class Droid:
    def __init__(self, name):        
        self.hidden_name = name        ##Esta variable no se puede nombrar fuera, por buena practica
    
    @property                          ##Lo que hace es ocultar el name a otros programadores
    def name(self) -> str:  #Convierte a name en un atributo
        return self.hidden_name
    
    @name.setter
    def name(self, name: str) -> None:
        self.hidden_name = name

android = Droid('Arthur')

print(android.name)
android.name = "Citripio"
print(android.name)

android.hidden_name = "Rojo"
print(android.hidden_name)
print(android.name)

print("----------------")

class CalculatedValue:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def get_calculated_value(self) -> float:
        return 0.35 * self.height
    
valuex = CalculatedValue("ratio", 10)

print(f"El {valuex.name} es: {valuex.get_calculated_value}")


print("----------------")

### Atributo de la clase: pertenece a la clase.
### Atributo de los objetos: viven en el objeto creado.

class Dog:
    obeys_owner = True

    def __init__(self, name):
        self.name = name 

dog_one = Dog("Burbuja")
dog_two = Dog("Isi")
dog_three = Dog("Fox")

print(f"{dog_one.name} obedece a su dueño {dog_one.obeys_owner}")
print(f"{dog_two.name} obedece a su dueño {dog_two.obeys_owner}")
print(f"{dog_three.name} obedece a su dueño {dog_three.obeys_owner}")

dog_two.obeys_owner = False 
print(f"{dog_one.name} obedece a su dueño {dog_one.obeys_owner}")
print(f"{dog_two.name} obedece a su dueño {dog_two.obeys_owner}")
print(f"{dog_three.name} obedece a su dueño {dog_three.obeys_owner}")

Dog.obeys_owner = True 
print(f"{dog_one.name} obedece a su dueño {dog_one.obeys_owner}")
print(f"{dog_two.name} obedece a su dueño {dog_two.obeys_owner}")
print(f"{dog_three.name} obedece a su dueño {dog_three.obeys_owner}")