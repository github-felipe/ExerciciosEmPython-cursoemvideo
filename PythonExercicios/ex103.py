def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gols no campeonato.'


nom = str(input('Nome: ')).strip()
gol = str(input('Gols: ')).strip()
if len(nom) > 0 and gol.isnumeric():
    gol = float(gol)
    if gol.is_integer():
        gol = int(gol)
        print(ficha(nom, gol))
elif len(nom) > 0:
    print(ficha(nom))
elif gol.isnumeric():
    gol = float(gol)
    if gol.is_integer():
        gol = int(gol)
        print(ficha(gols=gol))
else:
    print(ficha())
