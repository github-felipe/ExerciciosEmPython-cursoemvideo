valores = str(input('Digite o seu peso (Kg.) e altura (M.) separando-as por espaços: ')).strip()
peso = float(valores.split()[0])
altura = float(valores.split()[1])
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Você está abaixo do peso ideal, com o imc de {imc:.2f}!')
elif imc <= 25:
    print('Você está no peso ideal!')
elif imc <= 30:
    print(f'Você está em sobrepeso, com um imc de: {imc:.2f}!')
elif imc <= 40:
    print(f'Você está com obesidade, com um imc de: {imc:.2f}!')
else:
    print(f'Você está com obesidade mórbida, com um imc de {imc:.2f}!')
