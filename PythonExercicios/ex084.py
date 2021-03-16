pessoas = list()

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    if len(pessoas) == 0:
        maisPesado = peso
        maisLeve = peso
    else:
        if peso > maisPesado:
            maisPesado = peso
        if peso < maisLeve:
            maisLeve = peso
    dados = [nome, peso]
    pessoas.append(dados[:])
    dados.clear()
    while True:
        continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ').upper())
        if len(continuar) == 1:
            if continuar in 'NS':
                break
        print('Valor inválido, tente novamente...')
    if continuar.upper() == 'N':
        break

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

print(f'''Foram cadastradas um total de {len(pessoas)} pessoas.
O maior peso cadastrado foi: {maisPesado}Kg. Peso de: {nomeMaisPesado}.
O menor peso cadastrado foi: {maisLeve}Kg. Peso de: {nomeMaisLeve}.''')
