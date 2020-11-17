n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media <=5:
    cor = '\033[31m'
else:
    cor = '\033[32m'
print(f'Nota 1: {n1} \nNota 2: {n2} \nA sua média é: {cor}{media:.1f}\033[m')
