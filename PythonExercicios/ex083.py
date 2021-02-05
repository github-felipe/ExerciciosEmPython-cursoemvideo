exp = input('Digite uma expressão matemática para eu analisar se os parênteses estão corretos: ')
saldo = erro = 0
for x in exp:
    if x == '(':
        saldo += 1
    elif x == ')':
        saldo -= 1
    if saldo < 0:
        erro = 1
if saldo > 0:
    erro = 1
if erro == 0:
    print('A sua expressão é VÁLIDA')
elif erro == 1:
    print('A sua expressão é INVÁLIDA')
