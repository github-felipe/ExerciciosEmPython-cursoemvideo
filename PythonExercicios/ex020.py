from random import shuffle
a1 = str(input('Digite o nome de um aluno: '))
a2 = str(input('Digite o nome de outro aluno: '))
a3 = str(input('Digite o nome de mais outro aluno: '))
a4 = str(input('Digite o nome do último aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação é: \033[34m{lista}\033[m')
