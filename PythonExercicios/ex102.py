def fatorial(num, show=False):
    """
    fatorial(num, show=False)
    :param num: número no qual você deseja verificar o fatorial
    :param show: insira 'True' para se você deseja retornar, também, a resolução do cálculo desse fatorial
    :return: o fatorial do número inserido
    """
    result = str()
    passo = num
    final = 1
    for c in range(0, num):
        if c < num - 1:
            result += f'{passo} x '
        elif c == num - 1:
            result += f'{passo} = '
        final *= passo
        passo -= 1
    if show:
        result += f'{final}'
    else:
        result = str(final)
    result = f'''{"-" * (len(result) + 2)}
 {result} '''
    return result


print(fatorial(52, show=True))
print(fatorial(52))
print(fatorial(4, show=True))
