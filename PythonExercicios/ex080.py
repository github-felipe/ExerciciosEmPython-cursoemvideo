lista = list()
for c in range(0, 5):
    inserido = -1
    n = int(input('Digite um número: '))
    if c == 0:
        inserido = 0
        lista.append(n)
    else:
        for num in lista:
            if n < num:
                inserido = lista.index(num)
                break
        if inserido == -1:
            lista.append(n)
        else:
            lista.insert(inserido, n)
    if inserido == -1:
        print(f'O número {n} foi inserido no final da lista.')
    else:
        print(f'O número {n} foi inserido na posição {inserido} da lista.')
print(f'Lista final: {lista}')
