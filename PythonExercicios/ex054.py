from datetime import datetime
ano = datetime.today().year
n1 = int(input('Digite o ano de nascimento de uma pessoa: '))
n2 = 0
for c in range(0, 6):
    if ano - n1 >= 21:
        n2 = n2+ 1
    n1 = int(input('Digite o ano de nascimento de outra pessoa: '))
if ano - n1 >= 21:
    n2 = n2 + 1
print(f'Um total de {n2} das pessoas digitadas já tem ou terão nesse ano a maioridade')
