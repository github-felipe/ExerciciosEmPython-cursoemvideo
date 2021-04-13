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
