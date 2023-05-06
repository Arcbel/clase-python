peso_payaso = 112
peso_muñeca = 75

num_payasos = int(input('Ingrese cantidad de payasos: '))
num_muñecas = int(input('Ingrese cantidad de muñecas: '))

peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)
print(f'El peso total del envío es de {peso_total}')