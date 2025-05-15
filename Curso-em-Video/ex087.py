matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sl = list()
par = soma = 0
for c in range(0, 3):
    for l in range(0, 3):
        matriz[l][c] = int(input(f'Digite a linha {c+1} coluna {l+1}: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

for l in range(0, 3):
    soma += matriz[2][l]

for c in range(0, 3):
    sl.append(matriz[c][1])

print(f'O maior valor da segunda linha é {max(sl)}')
print(f'A soma da dos valores da terceira coluna é igual a {soma}')
print(f'A soma dos pares é igual a {par}')

for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[l][c]: ^5}]', end='')
    print()
