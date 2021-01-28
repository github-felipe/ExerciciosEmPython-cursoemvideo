print(f'''{"=" * 45}
CADASTRAMENTO DE NOVOS CLIENTES - CASAS BAHIA
{"=" * 45}''')
mais18 = homens = mulheres = 0
while True:
    continuar = 'a'
    idade = int(input('''Digite a idade '''))
    sexo = str(input('Digite o sexo [M/F]')).strip().upper()
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade > 20:
        mulheres += 1
    while continuar not in 'SN':
        continuar = str(input('''Quer continuar? [S/N]''')).strip().upper()
    if continuar == 'N':
        break
print(f'''
Foram cadastradas {mais18} pessoas com mais de 18 anos
Tivemos um total de {homens} homens cadastrados
Um total de {mulheres} mulheres com mais de 20 anos foram cadastradas
Término da operação, tenha um ótimo dia!''')
