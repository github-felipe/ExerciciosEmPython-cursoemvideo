from time import sleep
frase = str(input('Digite uma frase sem acentos: ')).strip()
print('Verificando se ela é um palíndromo... ')
sleep(0.3)
semEsp = frase.replace(' ', '').lower()
contrario = ''
n1 = len(semEsp)
for c in range(n1-1, -1, -1):
    contrario += f'{semEsp[c]}'
if contrario == semEsp:
    print(f'"{frase}" é um palíndromo!')
else:
    print(f'{frase} não é um palíndromo!')
#também poderia ser feito assim: frase3 = frase2[::-1]
