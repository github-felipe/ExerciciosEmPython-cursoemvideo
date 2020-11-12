print('Seja bem vindo(a) a calculadora de ano bissexto!')
ano = int(input('Digite um ano para ser verificado: '))
if (ano / 4).is_integer():
    if (ano / 100).is_integer():
        if (ano / 400).is_integer():
            print(f'O ano {ano} é bissexto!')
        else:
            print(f'O ano {ano} não é bissexto!')
    else:
        print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
