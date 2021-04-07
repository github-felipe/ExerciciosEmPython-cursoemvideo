def ficha(nome='<desconhecido>', gols='0'):
    return f'O jogador {nome} fez {gols} gols no campeonato.'


nom = str(input('Nome: '))
gol = str(input('Gols: '))
if len(nom) > 0 and len(gol) > 0:
    print(ficha(nom, gol))
elif len(nom) > 0:
    print(ficha(nom))
elif len(gol) > 0:
    print(ficha(gols=gol))
else:
    print(ficha())
