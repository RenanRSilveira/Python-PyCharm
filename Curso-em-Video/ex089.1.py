def linha():
    return print('-' * 42)


def main():  #PROGRAMA PRINCIPAL
    galera = []
    while True:
        try:
            while True:
                lista = []
                nome = input('Digite "fim" para cancelar! Nome: ').title()
                lista.clear()
                if nome.lower() == 'fim':
                    break
                n1 = float(input('Nota 1: '))
                n2 = float(input('Nota 2: '))
                media = (n1 + n2) / 2
                lista.append(nome)
                lista.append(n1)
                lista.append(n2)
                lista.append(media)
                galera.append(lista)
        except ValueError:
            print('Digite apenas valores válidos')
            continue
        break
    boletim(galera)
    notasIndividuais(galera)


def boletim(galera):
    linha()
    print('BOLETIM')
    linha()
    for i, v in enumerate(galera):
        print(f'ID: {i}   |   Nome: {v[0]}  |  Média: {v[3]}')
    linha()


def notasIndividuais(galera):
    print('Digite nada para finalizar')
    while True:
        try:
            while True:
                n = input('Digite o id do aluno para saber as notas individuais: ')
                linha()
                if n == '':
                    print('ENCERRANDO...')
                    break
                n = int(n)
                for i, v in enumerate(galera):
                    if i == n:
                        print(f'As notas de {i} são {v[1]} e {v[2]}')
                        linha()
        except ValueError:
            print('Digite um apenas números')
            continue
        break


if __name__ == '__main__':
    main()
