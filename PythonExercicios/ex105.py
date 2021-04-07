def notas(*n, sit=False):
    """
    -> Função para analisar notas de alunos que seguem um sistema padrão de ensino Brasileiro
    :param n: As notas dos alunos que devem ser analisadas
    :param sit: (opicional) indica se deve ou não adicionar a situação da turma
    :return: um dicionário contendo as informações já analisadas
    """
    valores = dict()
    valores['Total'] = len(n)
    valores['Maior nota'] = max(n)
    valores['Menor nota'] = min(n)
    total = 0
    for valor in n:
        total += valor
    media = total / len(n)
    valores['Média'] = media
    if sit:
        if media < 5:
            valores['Situação'] = 'RUIM'
        elif media < 7:
            valores['Situação'] = 'Razoável'
        else:
            valores['Situação'] = 'BOA'
    return valores


resp = notas(6, 10, 9, 5, 7, sit=True)
print(resp)
