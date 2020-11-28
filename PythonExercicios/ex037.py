print('\033[30;44m回回回回回回回回回回回回回回回回回回回回回回回\033[m' * 2)
print('\033[30;44mSeja muito bem vindo(a) ao melhor convertor de bases numéricas da atualidade!! \033[m')
print('\033[30;44m回回回回回回回回回回回回回回回回回回回回回回回\033[m' * 2)
valor = int(input('\033[30mDigite um número: \033[m'))
print('''\033[30mEscolha uma das bases abaixo para conversão
[ 1 ] Para BINÀRIO
[ 2 ] Para OCTAL
[ 3 ] Para HEXADECIMAL''')
escolha = int(input('\033[30mSua decisão: \033[m '))
if escolha == 1:
    print(f'\033[30mO valor de {valor} em binário é: {valor: b}\033[m')
elif escolha == 2:
    print(f'\033[30mO valor de {valor} em octal é: {valor: o}\033[m')
elif escolha == 3:
    print(f'\033[30mO valor de {valor} em hexadecimal é: {valor: x}\033[m')
else:
    print('\033[31mOpção inválida, tente novamente.\033[m')
#Também poderia ser feito assim:
# {bin(valor)[2:]}
# {oct(valor)[2:]}
# {hex(valor)[2:]}
