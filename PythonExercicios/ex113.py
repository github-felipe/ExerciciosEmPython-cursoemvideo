def leiaint(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except KeyboardInterrupt:
            n = 0
            print('\033[31mUsuário preferiu não digitar o número\033[m')
            break
        except Exception:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        else:
            break
    return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg).strip())
        except KeyboardInterrupt:
            n = 0
            print('\033[31mUsuário preferiu não digitar o número\033[m')
            break
        except Exception:
            print('\033[31mERRO! Digite um número real válido!\033[m')
        else:
            break
    return n


n1 = leiaint('Digite um número inteiro ')
n2 = leiafloat('Digite um número real')
print(f'Número inteiro digitado: {n1}. Número real digitado: {n2}')
