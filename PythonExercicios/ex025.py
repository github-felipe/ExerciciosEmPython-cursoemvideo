nome = str(input('Digite seu nome completo: '))
print(f'O nome \033[34m{nome}\033[m tem silva? \033[33m{"silva" in nome.lower()}\033[m')
