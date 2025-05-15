lista = list()
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < lista[pos]:
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1



print(lista)
