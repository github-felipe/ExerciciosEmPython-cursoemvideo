print('Digite "999" para parar o programa')
n = 0
total = 0
contador = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        total += n
        contador += 1
print(f'Você digitou um total de {contador} digitos e a soma de todos eles é: {total}')
