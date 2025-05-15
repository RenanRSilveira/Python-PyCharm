matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for l in range(0, 3):
        matriz[l][c] = int(input(f'Digite a coluna {c+1} linha {l+1}: '))

for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[l][c]: ^5}]', end='')
    print()