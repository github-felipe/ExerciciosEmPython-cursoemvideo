velocidade = int(input('Digite a velocidade atual do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    if velocidade > 159:
        print(f'\033[31mSe ferrou, vai ter que pagar uma multa de {multa} reais e ainda \033[30;41mperdeu a carteira de habilitação!\033[m')
    else:
        print(f'\033[31mSe ferrou, vai ter que pagar uma multa de {multa} reais!\033[m')
print('\033[30mTenha um ótimo dia!\033[m')
