time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'      Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break

print('Cód|Nome            |Gols          |Total')
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break

    if busca >= len(time):
        print('ERRO!')
    else:
        print(f'--Levantamento do jogador: {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'Na partida {i} fez {g} gols')
