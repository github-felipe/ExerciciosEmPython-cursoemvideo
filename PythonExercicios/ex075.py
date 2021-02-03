tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Os valores digitados foram: {tupla}')
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
print('Os valores pares digitados foram: ', end='')
pares = 0
for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')
        pares += 1
if pares == 0:
    print('Nenhum')
