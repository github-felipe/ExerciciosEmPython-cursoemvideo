n1 = int(input('Digite o começo de uma PA: '))
n2 = int(input('Agora digite a razão de uma PA: '))
contador = 0
while contador < 10:
    print(f'{n1 + (contador * n2)}', end=', ')
    contador += 1
print('Acabou')
