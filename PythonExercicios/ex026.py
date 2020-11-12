frase = str(input('Digite uma frase: ')).strip()
print(f'''Frase: {frase}
A letra "a" aparece {frase.lower().count("a")} vezes.
A primeira vez que a letra "a" aparece é na {int(frase.lower().find("a")) + 1}ª posição.
A última vez que a letra "a" aparece é na {int(frase.lower().rfind("a")) + 1}ª posição.''')
