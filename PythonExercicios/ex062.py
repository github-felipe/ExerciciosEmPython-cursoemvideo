n1 = int(input('Digite o começo de uma PA: '))
n2 = int(input('Digite a razão de uma PA: '))
contador = 0
quantidade = 10
while contador < quantidade:
    print(f'{n1 + contador * n2}', end=', ')
    contador +=1
    if contador == quantidade:
        quantidade += int(input('Você deseja ver mais quantos termos dessa progressão aritmética? '))
print('Fim')
