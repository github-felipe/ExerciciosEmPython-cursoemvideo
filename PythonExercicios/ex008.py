print('\033[31m┴┬┴┬┴┬┴┬┴┬┴┬\033[m'*5)
print('\033[30;41m Seja bem vindo ao melhor conversor de medidas do MUNDO!!!  \033[m')
print('\033[31m┴┬┴┬┴┬┴┬┴┬┴┬\033[m'*5)
m = float(input('Digite um valor em metros: '))
print(f'Quilômetros: \033[31m{m / 1000}\033[m km.')
print(f'Hectômetros: \033[31m{m / 100}\033[m hm.')
print(f'Decâmetros: \033[31m{m / 10}\033[m dam.')
print(f'Metros: \033[31m{m}\033[m m.')
print(f'Decimetros: \033[31m{m * 10}\033[m dm.')
print(f'Centímetros: \033[31m{m * 100}\033[m cm.')
print(f'Milímetros: \033[31m{m * 1000}\033[m mm.')
