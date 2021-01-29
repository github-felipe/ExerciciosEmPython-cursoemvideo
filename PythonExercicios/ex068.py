from random import randint
contador = ganhou = 0
print(f'''{"-=" * 13}
VAMOS JOGAR PAR OU IMPAR!!
{"-=" * 13}''')
while True:
    contador += 1
    escolha = 'a'
    jogador = int(input('Digite um número: '))
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    computador = randint(0, 10)
    print(f'Eu escolhi {computador}')
    print(f'A soma entre seu número e o do computador é: {computador + jogador}')
    par = ((jogador + computador)/2).is_integer()
    if escolha == 'P':
        if par:
            print(f'''Parabéns, você ganhou por ter escolhido par!!!
Quero revanche!!

{"=" * 20}
''')
            ganhou += 1
        else:
            break
    else:
        if not par:
            print(f'''Parabéns, você ganhou por ter escolhido ímpar!!!
Quero revanche!!!

{"=" * 20}
''')
            ganhou += 1
        else:
            break
print(f'Você teve um total de {ganhou} vitórias consecutivas!')
print(f'O recorde atual é de {contador * 827195340} vitórias consecutivas!')
