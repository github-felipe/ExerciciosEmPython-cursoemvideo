listagem = ('Pão', 0.8, 'Lápis', 1, 'Arroz', 10, 'monitor', 600, 'Suco de Pêra', 6, 'sorvete', 10)
print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)
print(f'Nome{"Valor":>36}')
for c in range(0, len(listagem)):
    if (c / 2).is_integer():
        print(f'{listagem[c]:.<31}', end='')
        tamanho = len(listagem[c])
    else:
        print(f'R${float(listagem[c]):>7.2f}')
print('=' * 40)
