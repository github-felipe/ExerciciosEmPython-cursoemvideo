pasta = open('cadastrados.txt')
linhas = pasta.readlines()
contador = 0
print('-' * 40)
for linha in linhas:
    linha = linha.replace('\n', '')
    if contador % 2 == 0:
        print(f'{linha:<31}', end='')
    else:
        print(f'{linha:>4} Anos')
    contador += 1
