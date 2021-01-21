n1 = n2 = int(input('Digite um número para ver seu fatorial: '))
fat = 1
quant = 0
while quant != n1:
    quant += 1
    fat *= n2
    print(f'\033[37m{n2}*', end='')
    n2 -= 1
print(f'= \033[m{fat}')

n1 = int(input('Digite outro número para ver seu fatorial: '))
fat = 1
for c in range(n1, 0, -1):
    fat *= c
    print(f'\033[37m{c}*', end='')
print(f'= \033[m{fat}')
