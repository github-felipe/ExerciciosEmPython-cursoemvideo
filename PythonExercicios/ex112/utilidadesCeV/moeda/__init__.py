def aumentar(n, porcento, formatado=False):
    multiplicador = porcento * 0.01
    final = n * multiplicador + n
    if formatado:
        final = moeda(final)
    return final


def diminuir(n, porcento, formatado=False):
    multiplicador = porcento * 0.01
    final = n - n * multiplicador
    if formatado:
        final = moeda(final)
    return final


def dobro(n, formatado=False):
    final = n * 2
    if formatado:
        final = moeda(final)
    return final


def metade(n, formatado=False):
    final = n / 2
    if formatado:
        final = moeda(final)
    return final


def moeda(n):
    final = f'R$:{n:.2f}'
    final = final.replace('.', ',')
    return final


def resumo(n, aumento, reducao):
    def mostrar(msg1, msg2):
        print(f'{msg1:<20}{msg2:>10}')
    valor = n
    print('_' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('_' * 30)
    mostrar('Valor analisado:', moeda(n))
    mostrar('Dobro do preço:', dobro(n, True))
    mostrar('Metade do preço:', metade(n, True))
    mostrar(f'{aumento}% de aumento:', aumentar(n, aumento, True))
    mostrar(f'{reducao}% de redução:', diminuir(n, reducao, True))
    print('_' * 30)
