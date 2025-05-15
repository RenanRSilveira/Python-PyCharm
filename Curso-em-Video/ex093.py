jogador = dict()
gols = []
jogador['nome'] = str(input('Nome do jogador: ').capitalize())
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    gol = int(input(f'Quantos gols na partida {c+1}? '))
    gols.append(gol)
jogador['gols'] = gols[:]
print('_'*30)
print(jogador)
print('-'*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*30)

print(f'O jogador {jogador["nome"]} jogou {tot} partidas')


for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {sum(gols)} gols')

