nome = str(input('Digite seu nome completo: '))
separado = nome.split()
n = len(separado)
print(f'''Nome: \033[34m{nome}\033[m
Primeiro nome: \033[34m{separado[0]}\033[m 
Último nome: \033[34m{separado[n-1]}\033[m''')
#Também poderia ser feito assim no final: print(f'último nome: {separado[len(separado) - 1]}') pra economisar uma linha de código
