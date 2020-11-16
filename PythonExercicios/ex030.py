n = int(input('Digite um número inteiro: '))
dividido = n / 2
if dividido.is_integer():
    print(f'O número {n} é par')
else:
    print(f'O número {n} é ímpar')
#Também poderia ser feito assim: resultado = n % 2
#if resultado == 0: print('Esse número é par')
#else: print('Esse número é ímpar')
