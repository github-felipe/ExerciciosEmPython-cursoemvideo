from random import randint
from time import sleep
jogadores = {}

print('Lista dos valores sorteados:')
for c in range(1, 5):
    sorteado = randint(1, 6)
    jogadores[f'jogador {c}'] = sorteado
    print(f'    Jogador {c} tirou {sorteado}')
    sleep(1)

ordenados = sorted(jogadores.values(), reverse=True)
banlist = list()
contador = 0

print('Lista com a ordem dos vencedores:')
for num in ordenados:
    contador += 1
    for item in jogadores.items():
        if item[1] == num:
            if item[0] not in banlist:
                jogador = item[0]
                banlist.append(jogador)
                break
    print(f'    {contador}º lugar: {jogador}, por tirar {num}')
    sleep(1)

print('Obrigado por usar o nosso programa, volte sempre!')
