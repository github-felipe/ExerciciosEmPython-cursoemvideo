from ex107 import moedas

p = float(input('Digite o preço R$:'))
print(f'R$:{p:.2f} mais 10% = R$:{moedas.aumentar(p, 10):.2f}')
print(f'R$:{p:.2f} menos 13% = R$:{moedas.diminuir(p, 13):.2f}')
print(f'A metade de R$:{p:.2f} é R$:{moedas.metade(p):.2f}')
print(f'O dobro de R$:{p:.2f} é R$: {moedas.dobro(p):.2f}')
