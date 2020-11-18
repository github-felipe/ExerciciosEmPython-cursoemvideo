salário = float(input('Digite o seu salário R$:'))
if salário >= 1250:
    print(f'O patrão ta generoso, o seu novo salário é \033[34mR${salário * 1.1:.2f}\033[m')
else:
    print(f'O patrão ta generoso, o seu novo salário é \033[34mR${salário * 1.15:.2f}\033[m')
