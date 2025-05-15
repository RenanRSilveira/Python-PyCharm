from Exemplo.text import *


def linha(tam=55):
    return print('-' * tam)


def menu():
    while True:
        try:
            while True:
                global resp
                linha()
                print('MENU PRINCIPAL'.center(55))
                linha()
                print('1- Ver pessoas cadastradas\n2- Cadastrar nova pessoa\n3- Sair do sistema')
                linha()
                resp = int(input('Sua opção: '))
                if resp == 1:
                    linha()
                    print('PESSOAS CADASTRADAS'.center(55))
                    linha()
                    verPessoas()
                    linha()
                if resp == 2:
                    linha()
                    print('CADASTRANDO NOVA PESSOA'.center(55))
                    linha()
                    adcPessoa()
                    linha()
                if resp == 3:
                    print('Saindo do sistema!')
                    break
        except ValueError:
            print('Digite um valor válido!')
        else:
            break
    return resp
