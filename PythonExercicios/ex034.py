salário = float(input('Digite o seu salário R$:'))
if salário >= 1250:
    print(f'O patrão ta generoso, o seu novo salário é R${salário * 1.1:.2f}')
else:
    print(f'O patrão ta generoso, o seu novo salário é R${salário * 1.15:.2f}')
