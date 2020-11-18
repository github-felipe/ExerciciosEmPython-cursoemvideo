from math import trunc
n = float(input('\033[30mDigite um número Real: '))
print(f'A porção inteira de {n} é {trunc(n)}')
#Ao invés de importar o trunc da biblioteca math dava pra escrever: print(f'A porção inteira de {n} é {int(n)}')
