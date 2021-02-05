lista = list()
contador = 0
while True:
    n = input('Digite um número [Ou uma letra para parar]: ')
    if not n.isnumeric():
        break
    else:
        n = int(n)
    if n in lista:
        print('Não considerarei esse valor pois já foi inserido na lista.')
    else:
        lista.append(n)
if len(lista) > 0:
    print(f'Os valores únicos digitados em ordem crescente são: {sorted(lista)}')
print('Obrigado por usar nosso programa, volte sempre!')
