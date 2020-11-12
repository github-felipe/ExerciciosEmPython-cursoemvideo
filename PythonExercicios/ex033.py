n = str(input('Digite 3 números diferentes, separando-os somente por espaço: ')).strip()
lista = n.split()
n1 = float(lista[0])
n2 = float(lista[1])
n3 = float(lista[2])
if n1 > n2:
    if n1 > n3:
        maior = n1
else:
    if n1 < n3:
        menor = n1
if n2 > n1:
    if n2 > n3:
        maior = n2
else:
    if n2 < n3:
        menor = n2
if n3 > n1:
    if n3 > n2:
        maior = n3
else:
    if n3 < n2:
        menor = n3
print(f'''O maior número é: {maior}
O menor número é: {menor}''')
#To orgulhoso desse código
