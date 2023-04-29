class CuentaBancaria():
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    
    def abono(self):
        self.monto = int(input("Ingrese monto a abonar: "))
        print(f"Se han abonado ${self.monto} a su cuenta.")
        self.saldo += self.monto
        print(f"Su saldo es: ${self.saldo}")

    def cargo(self):
        self.monto = int(input("Ingrese cargo: "))
        print(f"Se han cargado ${self.monto} a su cuenta.")
        self.saldo -= self.monto
        print(f"Su saldo es: ${self.saldo}")


cuenta_valeria_rojas = CuentaBancaria(18589124, 3000)

cuenta_valeria_rojas.abono()

cuenta_valeria_rojas.cargo()