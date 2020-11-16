from time import sleep
from random import randint
sorteado = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(2)
if n == sorteado:
    print('Parabéns, você acertou!!')
else:
    print(f'Você perdeu, eu pensei em {sorteado} e não em {n}!!')
