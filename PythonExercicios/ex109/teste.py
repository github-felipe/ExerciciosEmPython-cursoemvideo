from ex109 import moeda

p = float(input('Digite o preço R$:'))
print(f'{moeda.moeda(p)} mais 10% = {moeda.aumentar(p, 10, True)}')
print(f'{moeda.moeda(p)} menos 13% = {moeda.diminuir(p, 13, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
