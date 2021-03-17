estudante = {'Nome': str(input('Digite o nome: '))}
estudante['Média'] = int(input(f'Digite a média de {estudante["Nome"]}: '))
if estudante['Média'] < 5:
    estudante['Situação'] = 'Reprovado(a)'
else:
    estudante['Situação'] = 'Aprovado(a)'
for campo, valor in estudante.items():
    print(f'{campo} = {valor}')
