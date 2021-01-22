gen = 'a'
while gen not in 'MF':
    gen = str(input('Digite seu gênero [M/F]: ')).strip().upper()[0]
    if gen not in 'MF':
        print('O valor inserido está incorreto. Tente novamente.')
print(f'O gênero selecionado foi: {gen}')
