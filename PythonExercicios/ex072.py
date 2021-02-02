num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input('Digite um número entre 0 e 20: '))
while True:
    if -1 < escolha < 21:
        break
    else:
        escolha = int(input('Tente novamente... Escolha um número entre [0-20]: '))
print(f'O número escolhido é {num[escolha]}')
