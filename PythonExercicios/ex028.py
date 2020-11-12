from random import randint
sorteado = randint(0, 5)
n = int(input('Pensei em um número entre 0 e 5, tente adivinhar! '))
if n == sorteado:
    print('Parabéns, você acertou!!')
else:
    print('Burro d+ vc perdeu')
