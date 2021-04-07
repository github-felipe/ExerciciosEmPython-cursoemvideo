from time import sleep


def msg(string):
    print('~' * (len(string) + 2))
    print(f' {string} ')
    print('~' * (len(string) + 2))


while True:
    print('\33[30;42m', end='')
    msg('Sistema de ajuda PyHELP')
    user = str(input('\033[mFunção ou Biblioteca \033[32m>>>\033[m '))
    if user == 'fim':
        break
    print('\033[30;44m', end='')
    msg(f'Acessando o menu do comando {user}')
    sleep(1.5)
    print('\033[47m', end='')
    print(help(user))
print('\033[41mMuito obrigado por usar o sistema de ajuda PyHELP, volte sempre!')
