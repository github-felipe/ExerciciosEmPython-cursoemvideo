valor = float(input('Digite o valor do produto R$:'))
vezes = int(input('Digite em quantas vezes você pagará o produto: '))
if vezes == 1:
    meio = int(input('Qual é o meio de pagamento? digite 1 para dinheiro ou cheque ou então 2 para cartão: '))
    if meio == 1:
        print(f'O valor a ser pago é de: {valor * 0.9:.2f} a vista')
    elif meio == 2:
        print(f'O valor a ser pago é de: {valor * 0.95:.2f}')
else:
    if vezes == 2:
        print(f'O valor a ser pago é de duas vezes de R$:{valor / 2:.2f} no cartão')
    else:
        valor = valor * 1.2
        print(f'O valor a ser pago é de {vezes} vezes de R$:{valor / vezes:.2f}')
print('Tenha um ótimo dia!')
