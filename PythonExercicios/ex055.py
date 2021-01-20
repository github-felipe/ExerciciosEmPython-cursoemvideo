print('Obs: troque a vírgula "," por um ponto "."')
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso digitado é: {maior}Kg. e o menor é {menor}Kg.')
