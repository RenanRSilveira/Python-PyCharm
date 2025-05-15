from Exemplo.Menu import *


def verPessoas():
    with open('Pessoas.txt', 'r') as arq:
        print(arq.read())


def adcPessoa():
    with open('Pessoas.txt', 'a') as arq:
        try:
            nome = input('Nome: ').title()
            idade = int(input('Idade: '))
            x = 49 - len(nome)
            arq.write(f'\n{nome} {idade:>{x}} anos')
        except ValueError:
            print('Valor inválido')



