jogador = dict()
listaGols = list()
cadastros = list()
while True:
    totgols = 0
    print('-' * 20)
    nome = str(input('Nome: '))
    quant = int(input(f'Quantos jogos {nome} jogou? '))
    jogador['nome'] = nome
    for jogo in range(1, quant+1):
        gols = int(input(f'Gols feitos no {jogo}º jogo: '))
        totgols += gols
        listaGols.append(gols)
    jogador['gols'] = listaGols[:]
    jogador['totGols'] = totgols
    cadastros.append(jogador.copy())
    jogador.clear()
    listaGols.clear()
    continuar = str(input('Deseja cadastrar mais alguem? [S/N]')).upper()
    if continuar == 'N':
        break
print('-='*30)
print(f'ID Nome                Gols             Total')
print('_' * 45)
contador = 0
for jog in cadastros:
    print(f'{contador:>2} {jog["nome"]:<19} {str(jog["gols"]):<16} {jog["totGols"]:<5}')
    contador += 1
continuar = 0
while continuar != 999:
    print('-=' * 30)
    while True:
        escolha = int(input('Digite o ID do jogador que você quer ver os dados: (999 para parar)'))
        if escolha in range(0, contador) or escolha == 999:
            break
        print('Valor inválido, tente novamente...')
    if escolha == 999:
        break
    cont = 0
    for jogo in cadastros[escolha]['gols']:
        cont += 1
        print(f'Gols feitos no {cont}º jogo: {jogo}')
print('Muito obrigado por usar nosso programa, tenha um ótimo dia!')
