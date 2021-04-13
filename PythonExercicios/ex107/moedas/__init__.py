def aumentar(n, porcento):
    multiplicador = porcento * 0.01
    final = n * multiplicador + n
    return final


def diminuir(n, porcento):
    multiplicador = porcento * 0.01
    final = n - n * multiplicador
    return final


def dobro(n):
    final = n * 2
    return final


def metade(n):
    final = n / 2
    return final
