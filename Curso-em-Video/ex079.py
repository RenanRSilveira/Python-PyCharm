lista = list()
while True:
    n = (int(input('Digite um número: ')))
    if n not in lista:
        lista.append(n)
    else:
        print('Esse número já existe e não será adicionado')
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        print(sorted(lista))
        break
