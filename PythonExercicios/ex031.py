dist = float(input('Qual é a distância em quilômetros da sua viagem? '))
print(f'A distância da sua viagem é de {dist}Km.')
if dist >= 200:
    print(f'O valor a ser pago é de R${dist*0.5:.2f}')
else:
    print(f'O valor a ser pago é de R${dist*0.45:.2f}')
print('Tenha um bom dia!')
