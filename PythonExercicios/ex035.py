from time import sleep
print('-=-'*26)
print('Seja muito bem vindo(a) a melhor calculadora de triângulos do hemisfério sul!')
print('-=-'*26)
digitado = str(input('Digite o comprimento de 3 retas separando-as por espaços ')).strip()
separado = digitado.split()
n1 = float(separado[0])
n2 = float(separado[1])
n3 = float(separado[2])
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('estes segmentos PODEM formar um triângulo!')
else:
    print('Estes segmentos NÃO PODEM formar um triângulo!')
