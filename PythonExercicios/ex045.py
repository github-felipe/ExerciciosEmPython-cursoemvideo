from random import choice
escolhas = ['pedra', 'papel', 'tesoura']
computador = choice(escolhas)
bot = int(computador.replace('pedra', '1').replace('papel', '2').replace('tesoura', '3'))
print('\033[46;30m-=-\033[m'*25)
print('\033[46;30mVamos jogar pedra, papel ou tesoura, você consegue ganhar de mim, HUMANO???\033[m')
print('\033[46;30m-=-\033[m'*25)
jogador = str(input('\033[30mFaça sua escolha... \033[m')).strip().lower()
print(f'\033[30mescolhi {computador}...')
j1 = int(jogador.replace('pedra', '1').replace('papel', '2').replace('tesoura', '3'))
status = 1
if j1 == 1 and bot == 2:
    status = 0
elif j1 == 2 and bot == 3:
    status = 0
elif j1 == 3 and bot == 1:
    status = 0
if jogador == computador:
    print('\033[30mTa querendo me copiar??? escolhemos a mesma coisa!!!!\nRevanche!!!\033[m')
elif status == 1:
    print('\033[36mNem ferrando que você ganhou de mim... QUERO REVANCHE!!!!!\033[m')
elif status == 0:
    print('\033[31mHAHAHA VOCÊ PERDEU, HUMANO!!!!!')
