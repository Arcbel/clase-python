interes = 0.04
monto_inicial = int(input('Ingrese un monto inicial: '))

saldo_año_1 = (monto_inicial * interes) + monto_inicial
saldo_año_2 = (saldo_año_1 * interes) + saldo_año_1
saldo_año_3 = (saldo_año_2 * interes) + saldo_año_2

saldo_año_1_redondeado = round(saldo_año_1, 2)
saldo_año_2_redondeado = round(saldo_año_2, 2)
saldo_año_3_redondeado = round(saldo_año_3, 2)

print(f'Cantidad de ahorros para el primero año: {saldo_año_1_redondeado}')
print(f'Cantidad de ahorros para el segundo año: {saldo_año_2_redondeado}')
print(f'Cantidad de ahorros para el tercer año: {saldo_año_3_redondeado}')

