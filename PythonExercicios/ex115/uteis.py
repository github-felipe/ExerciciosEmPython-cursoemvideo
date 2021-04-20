def tab_cadastrados():
    pasta = open('cadastrados.txt')
    linhas = pasta.readlines()
    c = 0
    print('-'*40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('-'*40)
    for linha in linhas:
        linha = linha.replace('\n', '')
        if c % 2 == 0:
            print(f'{linha:<32}', end='')
        else:
            print(f'{linha:>3} Anos')
        c += 1


def aumentar(str1, str2):
    pasta = open('cadastrados.txt', 'a')
    pasta.write('\n' + str1)
    pasta.write('\n' + str2)
