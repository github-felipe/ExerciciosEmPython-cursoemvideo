from datetime import datetime
atual = int(datetime.today().date().year)
ano = int(input('Em qual ano você nasceu? '))
idade = atual - ano
if idade < 18:
    if 18 - idade == 1:
        print('Você deve se alistar ano que vem!!')
    else:
        print(f'Faltam {18 - idade} anos para você se alistar!')
elif idade == 18:
    print(f'Ja está na hora de se alistar!!')
else:
    print(f'Ja se passaram {idade - 18} anos desde o ano em que você era obrigado a se alistar!')
