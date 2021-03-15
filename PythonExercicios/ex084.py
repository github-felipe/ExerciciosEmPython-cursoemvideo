pessoas = list()
contador = 0
while True:
    contador += 1
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    if contador == 1:
        maisPesado = peso
        maisLeve = peso
    else:
        if peso > maisPesado:
            maisPesado = peso
        if peso < maisLeve:
            maisLeve = peso
    dados = [nome, peso]
    pessoas.append(dados[:])
    while True:
        continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ').upper())
        if len(continuar) == 1:
            if continuar in 'NS':
                break
        print('Valor inválido, tente novamente...')
    if continuar.upper() == 'N':
        break
    dados.clear()
nomeMaisPesado = str()
nomeMaisLeve = str()
for cadastro in pessoas:
    if cadastro[1] == maisPesado:
        if nomeMaisPesado == '':
            nomeMaisPesado = cadastro[0]
        else:
            nomeMaisPesado += f', {cadastro[0]}'
    if cadastro[1] == maisLeve:
        if nomeMaisLeve == '':
            nomeMaisLeve = cadastro[0]
        else:
            nomeMaisLeve += f', {cadastro[0]}'
print(f'''Foram cadastradas um total de {contador} pessoas.
O maior peso cadastrado foi: {maisPesado}Kg. Peso de: {nomeMaisPesado}.
O menor peso cadastrado foi: {maisLeve}Kg. Peso de: {nomeMaisLeve}.''')
