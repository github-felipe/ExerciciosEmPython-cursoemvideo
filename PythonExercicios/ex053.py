from time import sleep
frase1 = str(input('Digite uma frase sem acentos: ')).strip()
print('Verificando se ela é um palíndromo... ')
sleep(0.3)
frase2 = frase1.replace(' ', '').lower()
frase3 = ''
n1 = len(frase2)
for c in range(n1-1, -1, -1):
    frase3 = frase3 + f'{frase2[c]}'
if frase3 == frase2:
    print(f'"{frase1}" é um palíndromo!')
else:
    print(f'{frase1} não é um palíndromo!')
#também poderia ser feito assim: frase3 = frase2[::-1]
