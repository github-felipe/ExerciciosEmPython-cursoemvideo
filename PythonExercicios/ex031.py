dist = float(input('Qual é a distância em quilômetros da sua viagem? '))
print(f'A distância da sua viagem é de \033[34m{dist}Km\033[m.')
if dist <= 200:
    print(f'O valor a ser pago é de \033[34mR${dist*0.5:.2f}\033[m')
else:
    print(f'O valor a ser pago é de \033[34mR${dist*0.45:.2f}\033[m')
print('\033[30mTenha um bom dia!\033[m')
#Também poderia ter sido feito de forma simplificada: preço = dist * 0.5 if dist <=200 else dist * 0.45
