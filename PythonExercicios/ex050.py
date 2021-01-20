cont = 0
n = 0
for c in range(1, 7):
    x = int(input(f'Digite o {c}° número inteiro: '))
    n2 = x / 2
    if n2.is_integer():
        n += x
        cont += 1
if cont == 1:
    print(f'Você informou um número par que é: {n}')
else:
    print(f'Você informou {cont} números PARES e a soma deles é: {n}')
