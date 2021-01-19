print('Obs: troque a vírgula "," por um ponto "."')
n1 = float(input('Digite o peso de uma pessoa: '))
maior = 0
menor = n1
for c in range(0,4):
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    n1 = float(input('Digite o peso de outra pessoa: '))
if n1 > maior:
    maior = n1
if n1 < menor:
    menor = n1
print(f'O maior peso digitado é: {maior}Kg. e o menor é {menor}Kg.')