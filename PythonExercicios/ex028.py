from time import sleep
from random import randint
sorteado = randint(0, 5)
print('\033[36m-=-\033[m' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[36m-=-\033[m' * 19)
n = int(input('\033[30mEm qual número eu pensei?\033[m '))
print('Processando...')
sleep(2)
if n == sorteado:
    print('\033[30;44mParabéns, você acertou!!\033[m')
else:
    print(f';41mVocê perdeu, eu pensei em {sorteado} e não em {n}!!')
