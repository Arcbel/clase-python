class Banco():

    def __init__(self):
        self.cuentas = []  #guarda cuentas y correlativos
        self.movimientos = [] 

    def agregar_cuenta(self, _cuenta, _rut):
        self.cuentas.append({
            'cuenta': _cuenta,
            'rut': _rut,
            'correlativo_movimiento': 1,
            'saldo': 0
        })

    def agregar_movimiento(self, _cuenta, _fecha, _tipo, _monto):
        for elemento in self.cuentas:
            if elemento['cuenta'] == _cuenta:
                if _tipo == 'retiro':
                    if elemento['saldo'] - _monto < 0:
                        print('Saldo Insuficiente')
                    else:
                        self.movimientos.append({
                            'cuenta': _cuenta,
                            'correlativo_movimiento': elemento['correlativo_movimiento'],
                            'fecha': _fecha,
                            'tipo': _tipo,
                            'monto': _monto,
                            'saldo': elemento['saldo'] - _monto,
                        })
                        elemento['saldo'] = elemento['saldo'] - _monto
                        elemento['correlativo_movimiento'] = elemento['correlativo_movimiento'] + 1
                else:
                    self.movimientos.append({
                        'cuenta': _cuenta,
                        'correlativo_movimiento': elemento['correlativo_movimiento'],
                        'fecha': _fecha,
                        'tipo': _tipo,
                        'monto': _monto,
                        'saldo': elemento['saldo'] + _monto,
                    })
                    elemento['saldo'] = elemento['saldo'] + _monto
                    elemento['correlativo_movimiento'] = elemento['correlativo_movimiento'] + 1
                break

    def estado_cuenta (self, _cuenta):
        movimientos_cuenta = list(filter(lambda elementos: elementos['cuenta'] == _cuenta, self.movimientos))
        print("{:<20}".format(" Nº Mvto."),  "{:<20}".format("Fecha"),   "{:<20}".format("Tipo"),   "{:<20}".format("Monto"),  "{:<20}".format("Saldo"))
        for elemento in movimientos_cuenta:
            print("{:<20}".format(elemento['correlativo_movimiento']),  "{:<20}".format(elemento['fecha']),   "{:<20}".format(elemento['tipo']),   "{:<20}".format(elemento['monto']),  "{:<20}".format(elemento['saldo']))


banco_bci = Banco()

banco_bci.agregar_cuenta('77770', '13.444.555-1')
banco_bci.agregar_cuenta('77771', '13.444.555-2')
banco_bci.agregar_cuenta('77772', '13.444.555-3')
banco_bci.agregar_cuenta('77773', '13.444.555-4')

banco_bci.agregar_movimiento('77770', '17/04/23', 'abono', 2000)
banco_bci.agregar_movimiento('77770', '17/04/23', 'abono', 6000)
banco_bci.agregar_movimiento('77770', '17/04/23', 'retiro', 3000)

banco_bci.agregar_movimiento('77771', '17/04/23', 'abono', 12000)
banco_bci.agregar_movimiento('77771', '17/04/23', 'retiro', 4000)

banco_bci.agregar_movimiento('77772', '17/04/23', 'abono', 5000)

banco_bci.agregar_movimiento('77773', '17/04/23', 'abono', 8000)

banco_bci.estado_cuenta("77773")



