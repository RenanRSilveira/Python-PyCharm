s = 0
for c in range(1, 7):
    v = int(input('Digite um número inteiro: '))
    if v % 2 == 0:
        s += v
print(f'O somatório dos números pares digitado é {s}')
