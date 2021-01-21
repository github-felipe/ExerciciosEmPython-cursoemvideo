from random import randint
sorteado = randint(0, 10)
escolhido = 11
tentativas = 0
print('\033[36m-=-\033[m' * 19)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('\033[36m-=-\033[m' * 19)
while escolhido != sorteado:
    sorteado = randint(0, 10)
    escolhido = int(input('Em qual número eu pensei?: '))
    tentativas += 1
    if escolhido == sorteado:
        print(f'Parabéns!!!! Você acertou, eu realmente pensei em {sorteado}!!!')
    else:
        print('\033[30;41mVocê errou, tente novamente!\033[m \033[37m(obs: pensei em outro número)\033[m')
print(f'Você precisou de \033[36m{tentativas}\033[m tentativas para ganhar!')
