while True:
    n = int(input('Deseja ver a tabuada de qual número? '))
    print('='*36)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:2} = {n * c}')
    print('='*36)
print('NÃO TO AFIM DE CALCULAR A TABUADA DE NUMERO NEGATIVO.')
print('Obrigado pela preferência, vonte sempre!')
