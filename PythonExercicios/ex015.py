dias = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos quilômetros foram percorridos com o carro? '))
valor = (dias * 60)+(km * 0.15)
print(f'O carro foi alugado por {dias} dias e foram percorridos {km} quilômetros. O valor a ser pago é R$:{valor:.2f}')
