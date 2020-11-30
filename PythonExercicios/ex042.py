valores = str(input('Digite o comprimento de 3 retas separando-as por espaços: ')).strip()
n1 = float(valores.split()[0])
n2 = float(valores.split()[1])
n3 = float(valores.split()[2])
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Com o comprimento dessas retas é possível de se formar um triângulo!')
    if n1 == n2 == n3:
        print('E esse será um triângulo equilátero!')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('E esse será um triângulo isóceles!')
    else:
        print('E esse será um triângulo escaleno!')
else:
    print('Com esses comprimentos de retas não é possível de se formar um triângulo!!')
#também poderia ser feito assim:
#if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
#   print('é possível se formar um triângulo, ele é: ', end='')
#   if n1 == n2 == n3:
#       print('EQUILÁTERO')
#isso faria com que tudo ficasse na mesma linha de uma maneira mais rápida de se escrever
#obs: se x for igual a y, e y for igual a z, x é igual a z. Não tem necessidade de verificar se x é igual a z.
