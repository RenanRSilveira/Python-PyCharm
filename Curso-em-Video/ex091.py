from random import sample
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': sample((1, 6), 1),
        'Jogador 2': sample((1, 6), 1),
        'Jogador 3': sample((1, 6), 1),
        'Jogador 4': sample((1, 6), 1),
}
ranking = list()

for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(0.3)

ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} que tirou {v[1]}')
    sleep(0.2)