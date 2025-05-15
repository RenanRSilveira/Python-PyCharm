import estatistica


def porPartida():
    for k, v in enumerate(estatistica.jogador['gols']):
        print(f'Na partida {k+1} ele fez {v} gols')


def geral():
    if len(estatistica.jogadores) > 0:
        print(f'ID| Nome{" "*13}| Partidas{" "*6}| Gols')

        for i, v in enumerate(estatistica.jogadores):
            print(f'{i}   {v["nome"]}{" "*(18-len(v["nome"]))} '
                  f'{v["partidas"]}{" "*15}{v["total"]}')
        linha()
    else:
        pass


def linha():
    return print('-'*50)


def detalhes():
    while True:
        if len(estatistica.jogadores) > 0:
            while True:
                try:
                    busca = int(input('Mostrar os dados de qual jogador? [ID] '))
                    if len(estatistica.jogadores) > busca >= 0:
                        detalhe = estatistica.jogadores[busca]
                        linha()
                        print(f'-> Detalhes do jogador {detalhe["nome"]}:')
                        for k, v in enumerate(detalhe['gols']):
                            print(f'Na partida {k + 1} ele fez {v} gols')
                        linha()
                        break
                    else:
                        print('ID fora do alcance.')

                except(ValueError, IndexError):
                    print('Digite o número do ID de algum jogador que está na lista!')
        else:
            print('Nenhum jogador cadastrado.')
            break

        r = str(input('Deseja saber os dados de outro jogador? [S/N] ')).upper().strip()[0]
        while r not in 'SN':
            r = str(input('Deseja saber os dados de outro jogador? [S/N] ')).upper().strip()[0]

        if r == 'N':
            linha()
            print('Obrigado, volte sempre!')
            linha()
            break
        geral()
