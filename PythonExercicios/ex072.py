num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')
while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    while True:
        if 0 <= escolha <= 20:
            break
        else:
            escolha = int(input('Tente novamente... Escolha um número entre [0-20]: '))
    print(f'O número escolhido é {num[escolha]}')
    while True:
        escolha = str(input('Deseja continuar? [S/N]')).upper()
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
print('Obrigado por usar nosso programa, volte sempre!')
