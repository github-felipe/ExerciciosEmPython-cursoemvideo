n1 = int(input('Digite um número entre 0 e 9999 '))
n2 = n1 + 10000
n2 = str(n2)
print(f'Unidade: {n2[4]}')
print(f'Dezena: {n2[3]}')
print(f'Centena: {n2[2]}')
print(f'Milhar: {n2[1]}')
