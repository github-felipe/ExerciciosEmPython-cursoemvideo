from math import sqrt
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjascente: '))
print(f'Cateto oposto: {n1}')
print(f'Cateto adjascente: {n2}')
print(f'Hipotenusa: {sqrt(n1**2 + n2**2):.2f}')
#Também poderia ser feito usando o math.hypot(n1, n2) na sexta linha ao invés do math.sqrt(n1**2 + n2**2)
