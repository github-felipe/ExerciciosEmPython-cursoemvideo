alt = float(input('Digite a altura da parede em metros: '))
larg = float(input('Digite a largura da parede em metros: '))
area = alt * larg
tinta = area / 2
print('Especificações da parede:')
print(f'Altura: {alt}m. Largura: {larg}m.')
print(f'área: {area}m²')
print(f'Litros de tinta necessários: {tinta:.2f}')
