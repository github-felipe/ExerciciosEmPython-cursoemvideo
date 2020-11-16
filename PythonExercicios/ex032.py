from datetime import date
print('Seja bem vindo(a) a calculadora de ano bissexto!')
ano = str(input('Qual ano quer analisar? digite "atual" para analisar o ano atual: '))
if ano == 'atual':
    ano = date.today().year
ano = int(ano)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')
