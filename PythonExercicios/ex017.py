from math import sqrt
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjascente: '))
print(f'Cateto oposto: \033[32m{n1}\033[m')
print(f'Cateto adjascente: \033[34m{n2}\033[m')
print(f'Hipotenusa: \033[36m{sqrt(n1**2 + n2**2):.2f}\033[m')
#Também poderia ser feito usando o math.hypot(n1, n2) na sexta linha ao invés do math.sqrt(n1**2 + n2**2)
