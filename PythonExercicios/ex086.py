matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor para {linha, coluna}: '))
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')
    print('')
