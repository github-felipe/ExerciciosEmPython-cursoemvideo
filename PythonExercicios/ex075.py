tupla = (input('Digite um número: '), input('Digite outro número: '), input('Digite outro número: '),
         input('Digite outro número: '))
if 9 in tupla:
    if tupla.count(9) == 1:
        print('O número nove apareceu 1 vez')
    elif tupla.count(9) > 1:
        print(f'O número nove apareceu {tupla.count(9)} vezes')
else:
    print('Não foi digitado o número 9')
if 3 in tupla:
    print(f'A primeira vez em que o número três foi digitado foi na {tupla.index(3) + 1}ª posição')
else:
    print('Não foi digitado o número 3')
quantPares = 0
pares = ()
for c in range(0, 4):
    if int(tupla[c]) % 2 == 0:
        quantPares += 1
        par = tuple(tupla[c])
        pares2 = (pares, par)
        pares = pares2
        del pares2
if quantPares == 0:
    print('Não foram escritos números pares')
elif quantPares == 1:
    print(f'O número par escolhido foi: {pares[0]}')
elif quantPares == 2:
    print(f'Os números pares escolhidos foram: {pares[0]} e {pares[1]}')
else:
    print(f'Os números pares escolhidos foram: {str(pares).replace("(", "").replace(")", "").replace(",,", ",")[2:-1]}')
