from time import sleep
from random import randint


def sorteia(lista):
    print('Sorteando 5 valores na lista inserida:', end=' ')
    for c in range(0, 5):
        sorteado = randint(1, 9)
        print(sorteado, end=' ', flush=True)
        sleep(0.5)
        lista.append(sorteado)
    print('')


def somaPar(lista):
    pares_somados = 0
    for valor in lista:
        if valor % 2 == 0:
            pares_somados += valor
    print(f'Somando os valores pares de {lista} temos {pares_somados}.')


números = list()
sorteia(números)
somaPar(números)
