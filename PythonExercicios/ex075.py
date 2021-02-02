tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')),
         int(input('Digite outro número: ')))
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
par = 0
for c in range(0, 4):
    if tupla[c] / 2 == 0:
        par += 1
print(par)
