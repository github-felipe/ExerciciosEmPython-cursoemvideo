numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
    numeros[0] = sorted(numeros[0])
    numeros[1] = sorted(numeros[1])
print(f'''A lista de número pares é: {numeros[0]}
A lista de números ímpares é: {numeros[1]}''')
