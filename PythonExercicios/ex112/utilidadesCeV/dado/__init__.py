def leiadinheiro(v):
    def isfloat(v):
        try:
            float(v)
            return True
        except ValueError:
            return False
    while True:
        valor = str(input(v)).strip()
        formatado = valor.replace(',', '.')
        if isfloat(formatado):
            break
        print(f'\033[31mERRO. \"{valor}\" não é um valor númerico válido, tente novamente.\033[m')
    return float(valor.replace(',', '.'))
