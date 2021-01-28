from random import randint
contador = 0
print(f'''{"-=" * 13}
VAMOS JOGAR PAR OU IMPAR!!
{"-=" * 13}''')
while True:
    contador += 1
    jogador = int(input('Digite um número: '))
    escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    computador = randint(0, 10)
    print(f'Eu escolhi {computador}')
    par = ((jogador + computador)/2).is_integer()
    if escolha == 'P':
        if par:
            print(f'''Parabéns, você ganhou por ter escolhido par!!!
Quero revanche!!

{"=" * 20}
''')
        else:
            break
    else:
        if not par:
            print(f'''Parabéns, você ganhou por ter escolhido ímpar!!!
Quero revanche!!!

{"=" * 20}
''')
        else:
            break
print(f'Você perdeu na sua {contador}ª jogada!')
print(f'O recorde atual é de {contador * 827195340} vitórias consecutivas!')
