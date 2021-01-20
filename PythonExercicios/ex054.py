from datetime import datetime
ano = datetime.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    n = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if n > ano:
        print('foi digitado um valor inválido')
        erro = n + 'mensagem de erro pois foi escrito um valor maior que o ano atual'
    if ano - n >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo foram digitadas {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade.')
print('Obs: considerando o padrão estadunidense de 21 anos para a maioridade')
