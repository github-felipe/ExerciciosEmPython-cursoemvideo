n = str(input('Digite 3 números diferentes, separando-os somente por espaço: ')).strip()
lista = n.split()
n1 = float(lista[0])
n2 = float(lista[1])
n3 = float(lista[2])
maior = n1
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'''O maior número é: \033[1;36m{maior}\033[m
O menor número é: \033[1;34m{menor}\033[m''')
#Não to tão orgulhoso daquele código antigo mas ao menos aprendi 👌
