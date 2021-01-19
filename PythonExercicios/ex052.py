n = int(input('Digite um número: '))
verificador = 1
if (n / 2).is_integer() == False and n != 1 and n != 0:
    verificador = 0
    for c in range(2, n):
        n2 = n / c
        if n2.is_integer():
            verificador = 1
if verificador == 0:
    print('Esse número é primo!')
else:
    print('Esse número não é primo!')
