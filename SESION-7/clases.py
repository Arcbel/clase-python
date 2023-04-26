##Creando una clase

class Transporte:
    pass

class BuzzLightYear:
    pass

#Instanciar la clase (llamarla) y crear un objeto

transporte1 = Transporte()
transporte2 = Transporte()

buzz1 = BuzzLightYear()
buzz2 = BuzzLightYear()


print(type(transporte1))
print(type(buzz2))

print("---------------------------")

##Funciones y atributos en clases

class Droid:
    def __init__(self):  ##se usa para inicializar la clase
        self.power_on = False  ## el droid comienza apagado

    def switch_on(self): ## Self se incluye siempre
        print("Hola, soy un droid")
        self.power_on = True

    def switch_off(self):
        print("Adiós")
        self.power_on = False

k8_arthur = Droid()
k8_tripio = Droid()

k8_arthur.switch_on()
print("power on Arthur: ", k8_arthur.power_on)

k8_tripio.switch_off()
print("power on Tripio: ", k8_tripio.power_on)
k8_arthur.switch_off()
print("power on Arthur: ", k8_arthur.power_on)


print("---------------------------")

class Vehicle:
    def __init__(self, type, model):
        self.type_vehicle = type
        self.model_vehicle = model

sedan = Vehicle('Sedan', 'Aveo')
print(sedan.type_vehicle, sedan.model_vehicle)

pickup = Vehicle('Pickup', 'Ranger')
print(pickup.type_vehicle, pickup.model_vehicle)







