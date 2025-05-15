import Registro


def exibir_painel():
    print("\n--- Painel de Professores Registrados ---")
    print(f"{'ID':<5}{'Nome':<20}")
    print("-" * 30)

    for idx, prof in enumerate(Registro.professores, start=1):
        print(f"{idx:<5}{prof['nome']:<20}")

    print("-" * 30)
    print(f"Total de professores registrados: {len(Registro.professores)}")


def exibir_detalhes(id_professor):
    if 0 < id_professor <= len(Registro.professores):
        prof = Registro.professores[id_professor - 1]
        print("\n--- Detalhes do Professor ---")
        print(f"Nome: {prof['nome']}")
        print(f"E-mail: {prof['email']}")
        print(f"DDD: {prof['ddd']}")
        print(f"Telefone: {prof['telefone']}")
        print(f'Especialidade: ', end='')
        for x in prof['especializacoes']:
            print(f'{x} | ', end='')
        print()
        print("-" * 50)
    else:
        print("ID inválido. Tente novamente.")


def selecionar_prof():
    while True:
        exibir_painel()
        try:
            while True:
                id_professor = int(input("Digite o ID do professor para ver os detalhes (0 para sair): "))

                if id_professor == 0:
                    print("Encerrando o programa.")
                    return  # Sai da função e encerra o programa

                # Verifica se o ID é válido
                if 1 <= id_professor <= len(Registro.professores):
                    exibir_detalhes(id_professor)
                else:
                    print("ID inválido. Tente novamente.")
                    continue  # Solicita um novo ID

                # Pergunta se deseja ver outro professor
                while True:
                    try:
                        r = str(input('Deseja saber os detalhes de outro professor? [S/N] ')).upper().strip()[0]
                        if r in 'SN':
                            break
                        print('Resposta inválida. Digite "S" para Sim ou "N" para Não.')
                        exibir_painel()
                    except (ValueError, IndexError):
                        print('Digite um valor válido')

                if r == 'N':
                    print("Encerrando o programa.")
                    return  # Sai da função e encerra o programa

        except ValueError:
            print("Digite um número válido.")


def entrada():
    print('CADASTRO DE PROFESSORES'.center(30))


