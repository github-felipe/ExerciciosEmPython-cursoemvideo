from datetime import datetime
actYear = datetime.today().year
ctps = False
user = {'nome': str(input('Nome: ')), 'idade': actYear - int(input('Ano de nascimento: ')), 'ctps': str(input('Carteira de trabalho(0 para inexistente): '))}
if int(user['ctps']) > 0:
    user['ano de contratação'] = int(input('Ano de contratação: '))
    user['salário'] = float(input('Salário: '))
    user['aposentadoria'] = (user['idade'] + actYear) - user['ano de contratação'] + 35
    ctps = True
print(f'Nome: {user["nome"]}')
print(f'Idade: {user["idade"]}')
print(f'Carteira de trabalho: {user["ctps"]}')
if ctps:
    print(f'Ano de contratação: {user["ano de contratação"]}')
    print(f'Salário: {user["salário"]}')
    print(f'Se continuar nesse ritmo você se aposentará com {user["aposentadoria"]} anos!')
