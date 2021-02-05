numList = list()
while True:
    n = input('Digite um número [Ou uma letra para parar]: ')
    if n.isnumeric():
        n = int(n)
    else:
        break
    numList.append(n)
if len(numList) > 0:
    print('A lista está sendo organizada em ordem decrescente...')
    numList = sorted(numList, reverse=True)
    print(f'Foram digitados um total de {len(numList)} números')
    print(f'Lista em ordem decrescente é: {numList}')
    if 5 in numList:
        quant5 = numList.count(5)
        if quant5 > 1:
            print('O número 5 apareceu nas seguintes posições: ', end='')
        else:
            print('O número 5 apareceu na posição ', end='')
        last5 = contador = 0
        for c in range(0, quant5):
            contador += 1
            lugar = numList.index(5, last5)
            last5 = lugar + 1
            if contador == quant5:
                print(str(lugar) + '.')
            else:
                print(str(lugar), end=', ')
    else:
        print('Você não digitou o número 5!')
print('Obrigado por usar o nosso programa, volte sempre!')
