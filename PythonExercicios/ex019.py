from random import choice
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
print(f'O aluno(a) que deve apagar o quadro é: \033[31m{choice(lista)}\033[m')
