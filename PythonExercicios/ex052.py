n = int(input('Digite um número para verificá-lo se ele é ou não primo: '))
if n == 1:
    print('O número 1 não é considerado primo pois só pode ser dividido por 1 único número que é ele mesmo, e não 2 números.')
else:
    lista = []
    n = n + 1
    for c in range(1, n):
        x = [f'{c}']
        lista = lista + x
    otherlist = []
    novalista = []
    lista = lista[1:]
    for c in range(1, n - 1):
        y = [f'{lista[0]}']
        listazero = lista[0]
        otherlist = otherlist + y
        lista = lista[1:]
        for c in range(1, len(lista)-1):
            if (int((lista[c]) / listazero) / 2).is_integer():
                lista.remove(c)
    print(otherlist)