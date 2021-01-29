contador = total = maisDeMil = 0
print(f'''{"-" * 30}
{'CASAS VALIA':^30}
{"-" * 30}''')

while True:
    continuar = 'a'
    contador += 1
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto R$:'))

    if contador == 1 or valor < valorMaisBaixo:
        maisBarato = nome
        valorMaisBaixo = valor
    elif valor == valorMaisBaixo:
        maisBarato = maisBarato, nome

    total += valor
    if valor > 1000:
        maisDeMil += 1

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print(f'''O valor total da compra é: R${total:.2f}
Um total de {maisDeMil} produtos selecionados custam mais de R$:1000.00
O produto mais barato é: {maisBarato}, custando R${valorMaisBaixo:.2f}
Obrigado pela preferência, volte sempre!''')
