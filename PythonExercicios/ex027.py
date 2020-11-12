nome = str(input('Digite seu nome completo: '))
separado = nome.split()
n = len(separado)
print(f'''Nome: {nome}
Primeiro nome: {separado[0]} 
Último nome: {separado[n-1]}''')
#Também poderia ser feito assim no final: print(f'último nome: {separado[len(separado) - 1]}')
