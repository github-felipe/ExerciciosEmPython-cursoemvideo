from datetime import datetime
atual = datetime.today().year
nascimento = int(input('\033[30mDigite o ano de nascimento do(a) atleta: \033[m'))
print(f'Ano de nascimento: {nascimento}')
idade = atual - nascimento
if idade <= 9:
    print(f'\033[30mEste atleta tem {idade} anos. Classificação: MIRIM\033[m')
elif idade <= 14:
    print(f'\033[30mEste atleta tem {idade} anos. Classificação: INFANTIL\033[m')
    print('\033[37mVê se amadurece')
elif idade <= 19:
    print(f'\033[30mEste atleta tem {idade} anos. Classificação: JUNIOR\033[m')
elif idade <= 25:
    print(f'\033[30mEste atleta tem {idade} anos. Classificação: SÊNIOR\033[m')
else:
    print(f'\033[30mEste atleta tem {idade} anos. Classificação: MASTER\033[m')
