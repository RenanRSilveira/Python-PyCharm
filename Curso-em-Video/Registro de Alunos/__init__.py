def adicionar_aluno():
    while True:
        try:
            with open('alunos.txt', 'a', encoding='utf-8') as arquivo:
                nome = str(input('Nome: ')).capitalize()
                nota1 = float(input('Nota: '))
                nota = str(nota1)

                arquivo.write(f'{nome}: {nota}\n')
        except ValueError:
            pass

        resp = input('Deseja adicionar mais algum aluno? [S/N] ').upper()
        while resp not in 'SN' or not resp:
            resp = input('Deseja adicionar mais algum aluno? [S/N] ').upper()
        if resp == 'N':
            break


def ler_arquivo():
    with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome = linha.strip().split(': ')
            print(nome[0])


def buscar_aluno():
    try:
        busca = str(input('Deseja saber a nota de qual aluno? ')).capitalize().strip()
        encontrado = False
        with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome, nota = linha.strip().split(': ')
                if busca == nome:
                    encontrado = True
                    print(f'A nota de {nome} é {nota}')
            if not encontrado:
                print(f'Não encontrado')
    except ValueError:
        print('Valor inválido')


def linha():
    return print('-'*30)


def main():
    while True:
        linha()
        print('O que deseja fazer?\n'
              '1) Adicionar aluno\n'
              '2) Ver os alunos adicionados\n'
              '3) Saber a nota de um aluno\n'
              '4) Sair do programa')
        try:
            r = int(input('Sua opção: '))
            if r == 1:
                adicionar_aluno()
            elif r == 2:
                ler_arquivo()
            elif r == 3:
                buscar_aluno()
            elif r == 4:
                print('Obrigado!')
                break
            else:
                print('Opção inválida!')
        except ValueError:
            print('Valor inválido')


main()