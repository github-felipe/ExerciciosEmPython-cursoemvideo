n = str(input('Digite dois números: ')).strip()
n = n.split()
n1 = int(n[0])
n2 = int(n[1])
if n1 > n2:
    print('O PRIMEIRO número é maior')
elif n2 > n1:
    print('O SEGUNDO número é maior')
else:
    print('Não existe número maior, os dois são iguais!')
