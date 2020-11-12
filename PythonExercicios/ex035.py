print('Seja muito bem vindo(a) a melhor calculadora de triângulos do hemisfério sul!')
digitado = str(input('Digite o comprimento de 3 retas separando-as por espaços ')).strip()
print('Analisando...')
separado = digitado.split()
n1 = float(separado[0])
n2 = float(separado[1])
n3 = float(separado[2])
if abs(n2 - n3) < n1 < n2 + n3:
    if abs(n1 - n3) < n2 < n1 + n3:
        if abs(n1 - n2) < n3 < n1 + n2:
            print('Com essas retas é possível de se formar um triângulo!')
        else:
            print('Com essas retas não é possível de se formar um triângulo')
    else:
        print('Com essas retas não é possível de se formar um triângulo')
else:
    print('Com essas retas não é possível de se formar um triângulo')
