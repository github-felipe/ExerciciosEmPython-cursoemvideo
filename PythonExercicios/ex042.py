valores = str(input('Digite o comprimento de 3 retas separando-as por espaços: ')).strip()
n1 = float(valores.split()[0])
n2 = float(valores.split()[1])
n3 = float(valores.split()[2])
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Com o comprimento dessas retas é possível de se formar um triângulo!')
    if n1 == n2 and n1 == n3 and n2 == n3:
        print('E esse será um triângulo equilátero!')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('E esse será um triângulo isóceles!')
    else:
        print('E esse será um triângulo escaleno!')
else:
    print('Com esses comprimentos de retas não é possível de se formar um triângulo!!')
