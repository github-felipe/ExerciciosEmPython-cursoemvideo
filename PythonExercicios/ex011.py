alt = float(input('Digite a altura da parede em metros: '))
larg = float(input('Digite a largura da parede em metros: '))
area = alt * larg
tinta = area / 2
print('Especificações da parede:')
print(f'Altura: \033[1;32m{alt}\033[mm. Largura: \033[1;34m{larg}\033[mm.')
print(f'área: \033[1;36m{area}\033[mm²')
print(f'Litros de tinta necessários: \033[1;35m{tinta:.2f}\033[m')
