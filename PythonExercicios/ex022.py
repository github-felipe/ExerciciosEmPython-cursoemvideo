nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print('\033[1;36m'+nome.upper()+'\033[m')
print('\033[36m'+nome.lower()+'\033[m')
print(f'O seu nome possui \033[35m{len("".join(separado))}\033[m letras')
print(f'O seu primeiro nome possui \033[35m{len(separado[0])}\033[m letras')
#Ao invés de separar com o split eu poderia ter feito o terceiro print assim: print(f'O seu nome possui {len(nome) - nome.count(" ")} letras')
#no quarto print eu poderia ter feito assim: print(f'O seu primeiro nome possui {nome.find(" ")} letras')
