print('\033[33m┴┬┴┬┴┬┴┬┴┬┴┬┴┬\033[m' * 3)
print('\033[30mBem vindo(a) a MinhaCasa financiamentos!\033[m')
print('\033[33m┴┬┴┬┴┬┴┬┴┬┴┬┴┬\033[m' * 3)
print('\033[37mObs: Separe as informações com o uso de vírgulas ","\033[m')
info = str(input('\033[30mDigite na seguinte ordem: o valor da casa que você deseja comprar, o seu salário e em quantos anos você deseja pagar ela:\033[m ')).strip()
info = info.replace(',', ' ')
lista = info.split()
casa = float(lista[0])
salario = float(lista[1])
tempo = int(lista[2])
meses = tempo * 12
valor = casa / meses
if valor >= salario*0.3:
    print('\033[30mDesculpe mas seu financiamento foi \033[31mNEGADO\033[30m pois ele excede o limite máximo de 30% do salário.')
else:
    print(f'\033[30mAs prestações mensais são de : {meses}x de R$:{valor:.2f} sem juros!!!\033[m')
print('\033[36mTenha um ótimo dia e experimente calcular outros financiamentos nesta plataforma!!\033[m')