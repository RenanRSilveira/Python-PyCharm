professores = []


def registrar_professor():
    professor = {}
    try:
        while True:
            professor['nome'] = str(input('Nome do professor: ')).title()
            if professor['nome']:
                break
            else:
                print("O nome é obrigatório. Por favor, insira um nome válido.")

        while True:
            professor['email'] = str(input('E-mail: ')).strip().lower()
            if '@' and '.com' in professor['email']:
                break
            else:
                print("E-mail é obrigatório. Por favor, insira um e-mail válido.")
    except (ValueError, IndexError, TypeError):
        print('Cite valores válidos')

    while True:
        try:
            ddd = int(input('DDD: '))
            if len(str(ddd)) == 2:
                professor['ddd'] = ddd
                break
            else:
                print('O DDD deve conter 2 dígitos!')
        except (ValueError, IndexError):
            print('Cite valores válidos')

    while True:
        try:
            tel = int(input('Telefone: '))
            if len(str(tel)) == 9:
                professor['telefone'] = tel
                break
            else:
                print('O telefone deve conter 9 dígitos!')
        except (ValueError, IndexError):
            print('Cite valores válidos')

    # Lista de especializações disponíveis
    especializacoes = ['Ortodontia', 'Endodontia', 'Odontopediatria', 'Implantodontia']
    professor['especializacoes'] = []

    # Loop para adicionar múltiplas especializações
    while True:
        print("\nEscolha uma especialização para adicionar:")
        for i, esp in enumerate(especializacoes, start=1):
            print(f"{i} - {esp}")

        try:
            escolha = int(input("Digite o ID da especialização: "))
            if 1 <= escolha <= len(especializacoes):
                especializacao = especializacoes[escolha - 1]
                if especializacao not in professor['especializacoes']:
                    professor['especializacoes'].append(especializacao)
                    print(f"Especialização '{especializacao}' adicionada.")
                else:
                    print("Essa especialização já foi adicionada.")
            else:
                print("ID inválido. Escolha um número entre 1 e 4.")
        except ValueError:
            print("Digite um número válido.")

        # Pergunta se deseja adicionar outra especialização
        while True:
            try:
                r = str(input("Deseja adicionar outra especialização? [S/N] ")).upper().strip()[0]
                if r in 'SN':
                    break
                print('Resposta inválida. Digite "S" para Sim ou "N" para Não.')
            except (ValueError, IndexError):
                print('Digite um valor válido.')

        if r == 'N':
            break

    professores.append(professor.copy())


def inicio():
    while True:
        registrar_professor()
        while True:
            try:
                r = str(input('Deseja cadastrar outro professor? [S/N] ')).upper().strip()[0]
                if r in 'SN':
                    break
                print('Resposta inválida. Digite "S" para Sim ou "N" para Não.')
            except (ValueError, IndexError):
                print('Digite um valor válido')

        if r == 'N':
            break



