from random import randint
sorteados = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados são: {sorteados}')
print(f'O maior valor é: {sorted(sorteados)[-1]}')
print(f'O menor valor é: {sorted(sorteados)[0]}')
#Também poderia ser feito com os comandos: max(sorteados)    e    min(sorteados)
