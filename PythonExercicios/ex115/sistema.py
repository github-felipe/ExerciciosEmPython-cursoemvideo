from time import sleep
import arquivo
from lib import interface
arquivo.iniciar()
while True:
    interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    option = arquivo.leiaint('Sua opção:')
    if option == 1:
        arquivo.tab_cadastrados()
        sleep(2)
    elif option == 2:
        interface.cabeçalho('NOVO CADASTRO')
        while True:
            try:
                nome = str(input('Nome:'))
                num = 5 / len(nome)
            except Exception:
                print('\033[31mErro! Digite um valor válido!\033[m')
            else:
                break
        while True:
            try:
                idade = int(input('Idade:'))
                num = len(str(idade)) == 1 or 2 or 3
                idade = str(idade)
            except Exception:
                print('\033[31mErro! Digite um valor válido!\033[m')
            else:
                break
        arquivo.aumentar(nome, idade)
    elif option == 3:
        break
    else:
        print('\033[31mOpção inválida! tente novamente!\033[m')
