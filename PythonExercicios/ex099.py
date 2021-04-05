from time import sleep


def maior(*valores):
    print('-=' * 20)
    for c in range(0, len(valores)):
        if c < len(valores) - 1:
            print(valores[c], end=' ', flush=True)
            sleep(0.5)
        else:
            print(valores[c], end='. ', flush=True)
            sleep(0.5)
    maiorValor = 0
    if len(valores) > 0:
        maiorValor = max(valores)
    print(f'Foram informados {len(valores)} números.')
    print(f'O maior número informado foi: {maiorValor}')
    sleep(0.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
