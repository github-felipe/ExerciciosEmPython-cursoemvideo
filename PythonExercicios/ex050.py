n = 0
for c in range(0, 6):
    x = int(input('Digite um número inteiro: '))
    n2 = x / 2
    if n2.is_integer():
        n = n + x
print(f'A soma de todos os números pares que você digitou é: {n}')
