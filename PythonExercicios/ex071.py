print(f'''{"-" * 30}
{'Banco24h':^30}
{"-" * 30}''')
valor = int(input('Qual valor você deseja sacar? R$:'))
print('Está saindo do seu caixa:')
Cedula50 = Cedula20 = Cedula10 = Cedula1 = 0
while valor >= 50:
    Cedula50 += 1
    valor -= 50
if Cedula50 > 0:
    print(f'{Cedula50} Cédula(s) de R$50.00')
while valor >= 20:
    Cedula20 += 1
    valor -= 20
if Cedula20 > 0:
    print(f'{Cedula20} Cédula(s) de R$20.00')
while valor >= 10:
    Cedula10 += 1
    valor -= 10
if Cedula10 > 0:
    print(f'{Cedula10} Cédula(s) de R$10.00')
while valor >= 1:
    Cedula1 += 1
    valor -= 1
if Cedula1 > 0:
    print(f'{Cedula1} Cédula(s) de R$1.00')
