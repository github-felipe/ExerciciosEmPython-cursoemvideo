continuar = 'S'
contador = 0
total = 0
while continuar == 'S':
    valor = int(input('Digite um Valor: '))
    if contador == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    total += valor
    contador += 1
print(f'A média dos valores digitados é: {total / contador}')
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')
