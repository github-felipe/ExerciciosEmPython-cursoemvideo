from math import sqrt
n1 = int(input('Digite o valor do cateto oposto: '))
n2 = int(input('Digite o valor do cateto adjascente: '))
print(f'Cateto oposto: {n1}')
print(f'Cateto adjascente: {n2}')
print(f'Hipotenusa: {sqrt(n1**2 + n2**2):.2f}')
