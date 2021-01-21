n = int(input('Você deseja ver quantos termos da sequência de Fobonacci? '))
if n >= 0:
    n1 = 0
    n2 = 1
    contador = 0
    while contador < n:
        if contador == 0:
            print('\033[36m0\033[m->', end='')
        else:
            print(f'\033[36m{n2}\033[m->', end='')
            n3 = n2
            n2 = n1 + n2
            n1 = n3
        contador += 1
else:
    n1 = 0
    n2 = -1
    contador = 0
    while contador > n:
        if contador == 0:
            print('\033[36m0\033[m->', end='')
        else:
            print(f'\033[36m{n2}\033[m->', end='')
            n3 = n2
            n2 = n1 + n2
            n1 = n3
        contador -=1
print('Fim')