nome = str(input('Digite seu nome completo: '))
separado = nome.split()
n = len(separado)
print(f'''Nome: {nome}
Primeiro nome: {separado[0]} 
Último nome: {separado[n-1]}''')
