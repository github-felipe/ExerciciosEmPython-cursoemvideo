numList = list()
evenList = list()
oddList = list()
while True:
    n = input('Digite um número [Ou uma letra para parar]: ')
    if n.isnumeric():
        n = int(n)
    else:
        break
    numList.append(n)
if len(numList) > 0:
    for num in numList:
        if num % 2 == 0:
            evenList.append(num)
        else:
            oddList.append(num)
if len(numList) > 0:
    print(f'Lista completa: {numList}')
    print(f'Lista de números pares: {evenList}')
    print(f'Lista de números ímpares: {oddList}')
print('Obrigado por usar o nosso programa, volte sempre!')
