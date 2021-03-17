alunos = []
média = []
contador = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    alunos.append([nome, [n1, n2]])
    média.append((n1 + n2) / 2)
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ').upper())
        if len(continuar) == 1:
            if continuar in 'NS':
                break
        print('Valor inválido, tente novamente!')
    if continuar == 'N':
        break
    contador += 1
print('-=' * 11)
print('No. Nome        Média')
print('_'*22)
contador = 0
for aluno in alunos:
    print(f'{contador:<3} {aluno[0]:<11} {média[contador]:.1f}')
    contador += 1
print('-=' * 11)
while True:
    escolha = int(input('Você deseja ver as notas de qual aluno? (utilize o número dele na tabela) (999 para parar) '))
    if escolha == 999:
        break
    if escolha < len(alunos):
        print(f'''Aluno: {alunos[escolha][0]}
Nota 1: {alunos[escolha][1][0]}
Nota 2: {alunos[escolha][1][1]}
Média: {média[escolha]}''')
    else:
        print('Opção inválida, tente novamente...')
print('Muito obrigado por utilizar o nosso programa, volte sempre!!!')
