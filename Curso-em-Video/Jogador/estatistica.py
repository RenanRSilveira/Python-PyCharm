import programa
jogador = {}
jogadores = []

while True:
    try:
        jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
        jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
        gols = []

        for c in range(jogador['partidas']):
            gols.append(int(input(f'    ->Quantos gols fez na partida {c + 1}? ')))
        jogador['gols'] = gols.copy()
        jogador['total'] = sum(gols.copy())
        jogadores.append(jogador.copy())
        gols.clear()

    except (ValueError, IndexError):
        print('Cite valores válidos')

    while True:
        try:
            r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
            if r in 'SN':
                break
            print('Resposta inválida. Digite "S" para Sim ou "N" para Não.')

        except (ValueError, IndexError):
            print('Digite um valor válido')
    if r == 'N':
        programa.linha()
        break

