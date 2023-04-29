class Motocicleta:
    is_new = True
    motor = False

    def __init__(self, color, matricula, combustible_litros, numero_ruedas,
                marca, modelo, fecha_fabricacion,velocidad_punta, peso, maximo_combustible):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.maximo_combustible = maximo_combustible
    
    def arrancar(self):
        if self.motor == False:
            print("El motor ha arrancado")
        else:
            print("El motor ya estaba encendido")

    def detener(self):
        if self.motor == False:
            print("El motor ya estaba detenido")
        else: 
            print("El motor se ha detenido")

    def consultar_precio(self):
        print(f"El precio de la motocicleta {self.marca} {self.modelo} es ${self.precio}")

    def estado_repostaje(self):
        print(f"---Reporte de depósito de {self.marca} {self.modelo}---")
        print(f"La cantidad de combustible es de {self.combustible_litros} lts. La capacidad máxima es de {self.maximo_combustible} lts, por lo que faltan {self.maximo_combustible - self.combustible_litros} lts para llenar el depósito.")

    def nuevo_reposte(self):
        while True:
            try:
                self.reposte_litros = float(input("Indique la cantidad de combustible que quiere recargar en litros: "))
                if self.reposte_litros + self.combustible_litros <= self.maximo_combustible:
                    print(f"Has recargado {self.reposte_litros} lts.")
                    self.combustible_litros += self.reposte_litros 
                    print(f"El depósito tiene {self.combustible_litros} lts.")
                    break
                else:
                    print("La cantidad excede la capacidad del depósito. Inténtelo de nuevo.")
            except ValueError:
                print("Ingrese un valor numérico")


moto_1 = Motocicleta("Rojo", "CDF-78", 10, 2, "Yamaha", "Rage", "15 de Noviembre, 2022", 300, 100, 17)

moto_2 = Motocicleta(
    marca = "Yamaha",
    matricula = "KMC-79",
    modelo = "Black Spirit",
    color = "Negra",
    fecha_fabricacion = "15 de Noviembre, 2022",
    velocidad_punta = 280,
    combustible_litros = 0,
    numero_ruedas = 2,
    peso = 120,
    maximo_combustible = 20
    )

moto_1.arrancar()
moto_2.detener()

moto_1.precio = 9000
print(f"El precio de la motocicleta {moto_1.marca} {moto_1.modelo} es ${moto_1.precio}")

moto_1.consultar_precio()

moto_1.estado_repostaje()

moto_2.nuevo_reposte()

