matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceiraColuna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite o valor para {linha, coluna}: '))
        matriz[linha][coluna] = num
        if num % 2 == 0:
            pares += num
        if coluna == 2:
            terceiraColuna += num
maior = max(matriz[1])
print('-='*20)
for linha in matriz:
    for coluna in range(0, 3):
        if coluna == 2:
            print(f'[{linha[coluna]:^5}]')
        else:
            print(f'[{linha[coluna]:^5}]', end='')
print('-='*20)
print(f'''A soma dos valores pares é: {pares}
A soma dos valores da terceira coluna é: {terceiraColuna}
O maior valor da segunda linha é: {maior}''')
