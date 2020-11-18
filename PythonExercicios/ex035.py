from time import sleep
print('\033[34m-=-\033[m'*26)
print('\033[36mSeja muito bem vindo(a) a melhor calculadora de triângulos do hemisfério sul!\033[m')
print('\033[34m-=-\033[m'*26)
digitado = str(input('\033[30mDigite o comprimento de 3 retas separando-as por espaços\033[m ')).strip()
separado = digitado.split()
n1 = float(separado[0])
n2 = float(separado[1])
n3 = float(separado[2])
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[30mestes segmentos \033[34mPODEM\033[30m formar um triângulo!\033[m')
else:
    print('\033[30mEstes segmentos \033[31mNÃO PODEM\033[30m formar um triângulo!\033[m')
