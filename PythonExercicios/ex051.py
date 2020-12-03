n1 = int(input('Digite um número: '))
n2 = int(input('Digite a razão de uma PA: '))
n3 = n1 + n2 * 10
lista = ''
for c in range(n1, n3, n2):
    lista = lista + f'{c}, '
lista = lista[:len(lista)-2]
print(f'Os 10 primeiros números dessa progressão aritmética são: {lista}')
