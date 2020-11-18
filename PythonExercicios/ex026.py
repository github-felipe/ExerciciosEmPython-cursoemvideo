frase = str(input('Digite uma frase: ')).strip()
print(f'''Frase: \033[34m{frase}\033[m
A letra "a" aparece \033[35m{frase.lower().count("a")}\033[m vezes.
A primeira vez que a letra "a" aparece é na \033[35m{int(frase.lower().find("a")) + 1}ª\033[m posição.
A última vez que a letra "a" aparece é na \033[35m{int(frase.lower().rfind("a")) + 1}ª\033[m posição.''')
