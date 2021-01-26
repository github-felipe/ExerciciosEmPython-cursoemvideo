n1 = n2 = int(input('Digite um número para ver seu fatorial: '))
f = 1
quant = 0
while quant != n1:
    quant += 1
    f *= n2
    print(f'\033[37m{n2}', end='')
    print('*' if n2 > 1 else '= ', end='')
    n2 -= 1
print(f'\033[m{f}')

n1 = int(input('Digite outro número para ver seu fatorial: '))
f = 1
for c in range(n1, 0, -1):
    f *= c
    print(f'\033[37m{c}', end='')
    print('*' if c > 1 else '= ', end='')
print(f'\033[m{f}')
"""Também pode ser feito da seguinte forma:
from math import factorial
n = int(input('Digite um número'))
print(f'O fatorial de {n} é: {factorial(n)}')"""