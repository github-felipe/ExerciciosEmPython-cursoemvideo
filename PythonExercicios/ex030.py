n = int(input('Digite um número inteiro: '))
dividido = n / 2
if dividido.is_integer():
    print(f'O número \033[35m{n} \033[34mé par\033[m')
else:
    print(f'O número \033[35m{n} \033[31mé ímpar\033[m')
#Também poderia ser feito assim: resultado = n % 2
#if resultado == 0: print('Esse número é par')
#else: print('Esse número é ímpar')
