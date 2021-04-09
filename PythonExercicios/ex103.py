def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gols no campeonato.'


nom = str(input('Nome: ')).strip()
gol = str(input('Gols: ')).strip()
if gol.isnumeric():
    gol = float(gol)
    if gol.is_integer():
        gol = int(gol)
    else:
        gol = 0
else:
    gol = 0
if len(nom) > 0:
    print(ficha(nom, gol))
if len(nom) == 0:
    print(ficha(gols=gol))
