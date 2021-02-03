tupla = ('Python', 'chocolate', 'detergente', 'computador', 'doce', 'bombom', 'caneta', 'suco', 'mouse', 'Arroz')
for palavra in tupla:
    print(f'\nNa palavra {palavra} nós temos as vogais : ', end='')
    for letra in palavra:
        if letra in 'AEIOU aeiou':
            print(letra, end=' ')
