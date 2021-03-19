jogador = {'nome': str(input('Nome: '))}
lista = list()
totGols = 0
tot = int(input('Total de partidas jogadas: '))
if tot > 0:
    for partida in range(1, tot + 1):
        gols = (int(input(f'Gols feitos na {partida}ª partida: ')))
        lista.append(gols)
        totGols += gols
    jogador['gols'] = lista
    jogador['totGols'] = totGols
print('-=' * 20)
print(f'Nome: {jogador["nome"]}')
if tot > 1:
    contador = 0
    print(f'Lista dos gols feitos: {jogador["gols"]}')
    print(f'Total de gols: {jogador["totGols"]}')
    print('-=' * 20)
    for gol in jogador['gols']:
        contador += 1
        print(f'Gols feitos na {contador}ª partida: {gol}')
    print(f'Foi um total de {jogador["totGols"]} gols.')
else:
    print(f'Total de jogos jogados: {tot}')
print('-=' * 20)
print('Obrigado por usar o nosso programa, volte sempre!')
