from random import choice
from time import sleep
print('-='*20)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-='*20)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = list()
jogo = list()
valores = 0
for c in range(1, quant+1):
    valores = list(range(1, 61))
    for num in range(0, 6):
        valor = choice(valores)
        jogo.append(valor)
        valores.remove(valor)
    jogo.sort()
    print(f'Jogo {c}: {jogo}')
    sleep(1)
    jogo.clear()
    valores.clear()
print('Boa sorte!')
