from datetime import datetime
gen = str(input('Qual é o seu gênero? digite "m" para masculino ou "f" para feminino: ')).strip().lower()
if gen == 'm':
    atual = int(datetime.today().date().year)
    ano = int(input('Em qual ano você nasceu? '))
    idade = atual - ano
    if idade < 18:
        if 18 - idade == 1:
            print('Você deve se alistar no serviço militar ano que vem!!')
        else:
            saldo = 18 - idade
            print(f'Faltam {saldo} anos para você se alistar ao serviço militar!')
            print(f'Seu alistamento militar será em {atual + saldo}')
    elif idade == 18:
        print(f'Ja está na hora de se alistar ao serviço militar!!')
    else:
        if idade - 18 == 1:
            print('A data do seu alistamento militar foi ano passado!')
        else:
            saldo = idade - 18
            print(f'Já se passaram {saldo} anos desde o ano em que você era obrigado a se alistar no serviço militar!')
            print(f'O seu alistamento foi no ano de {atual - saldo}')
else:
    print('Você não precisa passar pelo alistamento militar obrigatório!')
