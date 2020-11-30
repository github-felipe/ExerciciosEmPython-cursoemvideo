from time import sleep
from random import choice
escolhas = ['pedra', 'papel', 'tesoura']
computador = choice(escolhas)
print('\033[46;30m-=-\033[m'*25)
print('\033[46;30mVamos jogar pedra, papel ou tesoura, você consegue ganhar de mim, HUMANO???\033[m')
print('\033[46;30m-=-\033[m'*25)
jogador = str(input('\033[30mFaça sua escolha... \033[m')).strip().lower()
print('\033[30mJO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
print(' ')
sleep(0.3)
print(f'\033[30mescolhi {computador}...')
print(' ')
status = 1
if jogador == 'pedra' and computador == 'papel':
    status = 0
elif jogador == 'papel' and computador == 'tesoura':
    status = 0
elif jogador == 'tesoura' and computador == 'pedra':
    status = 0
if jogador == computador:
    print('\033[30mTa querendo me copiar??? escolhemos a mesma coisa!!!!\nRevanche!!!\033[m')
elif status == 1:
    print('\033[36mVocê ganhou de mim??? QUERO REVANCHE!!!!')
elif status == 0:
    print('\033[31mHAHAHA VOCÊ PERDEU, HUMANO!!!!!')
