lpar = []
limpar = []
lista = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lpar.append(n)
        lista.append(n)
    else:
        limpar.append(n)
        lista.append(n)
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print(f'A lista completa é {lista}')
print(f'Os valores pares são {lpar}')
print(f'Os valores ímpares são {limpar}')
