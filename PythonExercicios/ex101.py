def voto(nascimento):
    from datetime import datetime
    hoje = datetime.today().year
    idade = hoje - nascimento
    if idade < 16:
        return f'Idade {idade}: Voto NEGADO'
    elif 15 < idade < 18:
        return f'Idade {idade}: Voto OPICIONAL'
    elif 65 > idade > 17:
        return f'Idade {idade}: Voto OBRIGATÓRIO'
    elif idade > 64:
        return f'Idade {idade}: Voto OPICIONAL'


print('-' * 30)
nasceu = int(input('Digite seu ano de nascimento: '))
print(voto(nasceu))
