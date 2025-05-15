lista = []
galera = []


def linha(tam=42):
    return '-' * tam


while True:
    try:
        while True:
            lista.clear()
            nome = str(input('Nome: ')).title()
            n1 = float(input('Nota 1: '))
            n2 = float(input('Nota 2: '))
            media = (n1 + n2) / 2
            lista.append(nome)
            lista.append(n1)
            lista.append(n2)
            lista.append(media)
            galera.append(lista.copy())
            try:
                while True:
                    r = str(input('Deseja continuar? [S/N]: ')).upper().strip()
                    if r == 'N' or r == 'S':
                        break
                    elif not r:
                        print('Por favor, responda com S ou N')
                        continue
                    else:
                        print('Digite apenas S ou N')
                if r == 'N':
                    break

            except(ValueError, IndexError):
                print('ERRO')

        print(linha())
        print(f'{"ID":<4}{"NOME"} {"MÉDIA":>33}')
        for i, v in enumerate(galera):
            x = 35 - len(v[0])
            print(f'{i}   {v[0]} {v[3]:>{x}}')
        print(linha())

    except(ValueError, SyntaxError, TypeError):
        print('DIGITE OS VALORES CORRETAMENTE')
        continue
    break


while True:
    try:
        print(linha())
        print('Digite nada para cancelar')
        print(linha())
        ent = input('Deseja saber a nota de qual aluno? [ID]: ')

        if ent == '':
            break
        x = int(ent)
        for i, v in enumerate(galera):
            if i == x:
                print(linha())
                print(f'As notas de {v[0]} são {v[1]} e {v[2]}')
    except ValueError:
        print(end='')
