idade = int(input('\033[30mDigite a idade do(a) atleta: \033[m'))
if idade <= 9:
    print(f'\033[30mCom a idade de {idade} anos este atleta é considerado(a) MIRIM\033[m')
elif idade <= 14:
    print(f'\033[30mCom a idade de {idade} anos este atleta é considerado(a) INFANTIL\033[m')
    print('\033[37mVê se amadurece')
elif idade <= 19:
    print(f'\033[30mCom a idade de {idade} anos este atleta é considerado(a) JUNIOR\033[m')
elif idade <= 20:
    print(f'\033[30mCom a idade de {idade} anos este atleta é considerado(a) SÊNIOR\033[m')
else:
    print(f'\033[30mCom a idade de {idade} anos este atleta é considerado(a) MASTER\033[m')
