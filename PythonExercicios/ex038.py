n = str(input('Digite dois números: ')).strip()
n = n.split()
n1 = int(n[0])
n2 = int(n[1])
if n1 > n2:
    print(f'O maior número é {n1} e o menor número é {n2}')
elif n2 > n1:
    print(f'O maior número é {n2} e o menor número é {n1}')
else:
    print('Não existe número maior, os dois são iguais!')
