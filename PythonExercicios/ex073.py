classificação = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'Ceará SC', 'Corinthians',
                 'Santos', 'Atlético-GO', 'Bragantino', 'Vasco da Gama', 'Bahia', 'Sport Recife', 'Fortaleza', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Os 5 melhores times no brasileirão atual é: {classificação[:5]}')
print(f'Os times que estão no top 4 ao contário são: {classificação[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(classificação)}')
print(f'Chapecoense não está mais na série A...')
print(f'Já São Paulo está na posição: {classificação.index("São Paulo") + 1}')
