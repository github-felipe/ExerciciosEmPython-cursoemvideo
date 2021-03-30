def area(larg, comp):
    print(f'A área de um terreno {larg} X {comp} é: {larg * comp}M².')


print('Controle de terrenos')
print('-'*20)
la = float(input('Digite a largura em Metros: '))
c = float(input('Digite o comprimento em Metros: '))
area(la, c)
