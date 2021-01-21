from time import sleep
option = 0
while option != 5:
    n1 = float(input('\033[33mDigite um valor:\033[m '))
    n2 = float(input('\033[33mDigite outro valor:\033[m '))
    print('''\033[36m[1]\033[m somar
\033[36m[2]\033[m multiplicar
\033[36m[3]\033[m maior
\033[36m[4]\033[m novos números
\033[36m[5]\033[m sair do programa''')
    option = int(input('\033[33mSelecione uma opção:\033[m '))
    if option == 1:
        print(f'{n1} + {n2} = {n1+n2}')
        sleep(3)
    if option == 2:
        print(f'{n1} X {n2} = {n1*n2}')
        sleep(3)
    if option == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior desses dois números é: {maior}')
        sleep(3)
print('Obrigado por utilizar nosso programa!')