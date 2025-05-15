lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
q = len(lista)
d = sorted(lista, reverse=True)
print(f'Foram digitados {q} números!')
print(f'A ordem decrescente é {d}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 \033[31mNÃO\033[m está na lista')