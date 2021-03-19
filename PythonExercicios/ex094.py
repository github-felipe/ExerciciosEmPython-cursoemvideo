contador = 0
totIdade = 0
cadastros = list()

while True:
    contador += 1
    nom = str(input('Nome: '))
    while True:
        gen = str(input('Gênero: [M/F] ')).upper()
        if len(gen) == 1:
            if gen in 'MF':
                break
        print('Valor inválido, tente novamente...')
    idade = int(input('Idade: '))
    totIdade += idade
    if gen == 'M':
        mUsuario = {'nome': nom, 'genero': gen, 'idade': idade}
        cadastros.append(mUsuario.copy())
        mUsuario.clear()
    if gen == 'F':
        fUsuaria = {'nome': nom, 'genero': gen, 'idade': idade}
        cadastros.append(fUsuaria.copy())
        fUsuaria.clear()
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar == 'N':
        break

listaF = list()
media = totIdade / contador

for cadastro in cadastros:
    if cadastro['genero'] == 'F':
        listaF.append(cadastro['nome'][:])

print('-=' * 20)
print(f'Foram cadastradas um total de {contador} pessoas.')
print(f'A média de idade do grupo é de: {media} anos.')
print(f'As mulheres cadastradas foram: {listaF}.')
print(f'As pessoas com idade acima da média são:')

for cadastro in cadastros:
    if cadastro['idade'] > media:
        print('')
        print(cadastro)

print('Muito obrigado por usar nosso programa, volte sempre!')
