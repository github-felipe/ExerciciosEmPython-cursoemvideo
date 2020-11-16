velocidade = int(input('Digite a velocidade atual do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    if velocidade > 159:
        print(f'Se ferrou, vai ter que pagar uma multa de {multa} reais e ainda perdeu a carteira de habilitação!')
    else:
        print(f'Se ferrou, vai ter que pagar uma multa de {multa} reais!')
print('Tenha um ótimo dia!')
