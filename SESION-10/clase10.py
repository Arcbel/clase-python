class Droid:
    def __init__(self, name):        
        self.__name = name 
    
    @property                   
    def name(self) -> str:  
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

arturo = Droid("Arturo")

print(arturo.name)
#print(arturo.__name)

class Artefacto:
    def __init__(self, color, peso, marca):
        self.__color = color
        self.__peso = peso
        self.__marca = marca

    @property
    def color(self) -> str:
        return self.__color
    @color.setter
    def color(self, color: str) -> None:
        self.__color = color
    
    @property
    def peso(self) -> float:
        return self.__peso
    @peso.setter
    def peso(self, peso: float) -> None:
        self.__peso = peso

    @property
    def marca(self) -> str:
        return self.__marca
    @marca.setter
    def marca(self, marca: str) -> None:
        self.__marca = marca

linterna = Artefacto("Negra", 1, "Switch")
linterna.color = "blanca"
print(linterna.color)


