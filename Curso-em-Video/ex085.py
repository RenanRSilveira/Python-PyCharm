lista = [[], []]
n = 0
for c in range(0, 7):
    n = (int(input('Digite um número: ')))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 != 0:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
if len(lista[0]) > 0:
    print(f'Os pares são {lista[0]}')
else:
    print('Não temos números pares')
if len(lista[1]) > 0:
    print(f'Os ímpares são {lista[1]}')
else:
    print('Não temos números ímpares')