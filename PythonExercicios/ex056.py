from time import sleep
media = 0
velho = 0
maisvelho = 'erro 404'
quantidade = 0
for c in range(0, 4):
    print('')
    print('')
    print('')
    print('Seja muito bem vindo(a) à nasa!!!!! Parabéns por passar em nosso processo seletivo!!!')
    print('-='*5, 'Iniciando ficha de cadastro para: \033[36mestágio\033[m ', '-='*5)
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade atual: '))
    gen = str(input('Qual é o seu gênero? digite \033[34mF\033[m para feminino, \033[34mM\033[m para masculino ou \033[34mX\033[m para nenhuma das anteriores/ indefinide: ')).upper().strip()
    print('Você acabou de terminar seu cadastro!!! Agora siga a faixa \033[32mverde\033[m no chão e espere a chamada de seu NCP(Número de Cadastro Provisório)!')
    media = media + idade
    if gen == 'M':
        if idade > velho:
            maisvelho = nome
            velho = idade
    if gen == 'F':
        if idade < 20:
            quantidade = quantidade + 1
    sleep(5)
print('')
print('')
print('')
media = media / 4
print(f'A média de idade das pessoas inscritas neste terminal é de: {media}')
print(f'O nome do homem mais velho inscrito neste terminal tem {velho} anos e se chama: {maisvelho}')
if quantidade == 1:
    print('Apenas uma mulher com menos de 20 anos foi inscrita neste terminal')
else:
    print(f'{quantidade} Mulheres com menos de 20 anos foram inscritas neste terminal')
