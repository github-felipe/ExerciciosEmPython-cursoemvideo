def iniciar():
    try:
        open('cadastrados.txt')
    except FileNotFoundError:
        open('cadastrados.txt', 'wt+')


def tab_cadastrados():
    pasta = open('cadastrados.txt')
    linhas = pasta.readlines()
    c = 0
    print('-'*40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('-'*40)
    for linha in linhas:
        linha = linha.replace('\n', '')
        linha = linha.split(';')
        print(f'{linha[0]:<32}{linha[1]:>3} anos')


def aumentar(str1, str2):
    pasta = open('cadastrados.txt', 'a')
    pasta.write('\n' + str1 + ';' + str2)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except KeyboardInterrupt:
            n = 0
            print('\033[31mUsuário preferiu não digitar o número\033[m')
            break
        except Exception:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
        else:
            break
    return n
