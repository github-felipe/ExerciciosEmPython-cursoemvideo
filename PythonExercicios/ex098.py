from time import sleep


def contar(ini, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    print('-=' * 30)
    print(f'Contagem de {ini} até {fim}, de {passo} em {passo}')
    atual = ini
    if ini < fim:
        while True:
            if atual <= fim:
                print(atual, end=' ', flush=True)
            else:
                print('FIM!')
                sleep(1)
                break
            atual += passo
            sleep(0.5)
    else:
        while True:
            if atual >= fim:
                print(atual, end=' ', flush=True)
            else:
                print('FIM!')
                sleep(1)
                break
            atual -= passo
            sleep(0.5)


contar(1, 10, 1)
contar(10, 0, 2)
print('')
print('Agora é a sua vez!\n')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contar(inicio, fim, passo)
