lista = list()
for c in range(0, 5):
    n = int(input(f'Digite um número para a posição {c} na lista: '))
    lista.append(n)
max = max(lista)
quantmax = lista.count(max)
min = min(lista)
quantmin = lista.count(min)
if lista.count(max) > 1:
    print(f'O maior valor digitado foi: {max} e ele apareceu nas posições: ', end='')
else:
    print(f'O maior valor digitado foi: {max} e ele apareceu na posição: ', end='')
contador = 0
lastMax = 0
for n in range(0, quantmax):
    contador += 1
    if contador == quantmax:
        print(str(lista.index(max, lastMax)) + '.')
    else:
        print(lista.index(max, lastMax), end=', ')
        lastMax = lista.index(max, lastMax) + 1
if lista.count(min) > 1:
    print(f'O menor valor digitado foi: {min} e ele apareceu nas posições: ', end='')
else:
    print(f'O menor valor digitado foi: {min} e ele apareceu na posição: ', end='')
contador = 0
lastMin = 0
for n in range(0, quantmin):
    contador += 1
    if contador == quantmin:
        print(str(lista.index(min, lastMin)) + '.')
    else:
        print(lista.index(min, lastMin), end=', ')
        lastMin = lista.index(min, lastMin) + 1
