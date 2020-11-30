print(f'{" LOJAS LIMA ":=^40}')
valor = float(input('Digite o valor da compra R$:'))
print('''Formas de pagamento
[ 1 ] À vista no dinheiro/ cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
escolha = int(input('Qual a opção? '))
if escolha == 1:
    print(f'O valor a ser pago é de R${valor * 0.8:.2f}')
elif escolha == 2:
    print(f'O valor a ser pago é de R${valor * 0.9:.2f}')
elif escolha == 3:
    print(f'O valor a ser pago é de duas vezes de R${valor / 2:.2f} totalizando R${valor:.2f}')
elif escolha == 4:
    valor = valor * 1.2
    parcelas = int(input('Será pago em quantas parcelas? '))
    print(f'O valor a ser pago é de {parcelas}x de R${valor / parcelas:.2f} totalizando R${valor:.2f}')
else:
    print('Valor inválido, tente novamente')
print('Tenha um ótimo dia!')
