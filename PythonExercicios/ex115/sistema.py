from time import sleep
import uteis
while True:
    print('-' * 40)
    print(f'{"Menu Principal":^40}')
    print('-' * 40)
    print('\033[1;33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[1;33m2\033[m - \033[34mCadastrar nova pessoa\033[m')
    print('\033[1;33m3\033[m - \033[34mSair do sistema\033[m')
    print('-' * 40)
    try:
        option = int(input('\033[33mSua opção: \033[m'))
    except Exception:
        print('\033[31mOpção inválida! tente novamente!\033[m')
        sleep(1)
    else:
        if option == 1:
            uteis.tab_cadastrados()
            sleep(2)
        elif option == 2:
            print('-' * 40)
            print(f'{"NOVO CADASTRO":^40}')
            print('-' * 40)
            while True:
                try:
                    nome = str(input('Nome:'))
                    num = 5 / len(nome)
                except Exception:
                    print('\033[31mErro! Digite um valor válido!\033[m')
                else:
                    break
            while True:
                try:
                    idade = int(input('Idade:'))
                    num = len(str(idade)) == 1 or 2 or 3
                    idade = str(idade)
                except Exception:
                    print('\033[31mErro! Digite um valor válido!\033[m')
                else:
                    break
            uteis.aumentar(nome, idade)
        elif option == 3:
            break
        else:
            print('\033[31mOpção inválida! tente novamente!\033[m')
