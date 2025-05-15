lista = list()
galera = list()
maior = menor = 0
while True:
    lista.append(str(input('Nome: ')).capitalize())
    lista.append(float(input('Peso (kg): ')))
    if len(galera) == 0:
        maior = menor = lista[1]
        nmaior = nmenor = lista[0]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    galera.append(lista[:])
    lista.clear()
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break

print(f'Foram cadastradas {len(galera)} pessoas')
print(f'O maior peso foi {maior} kg de', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menor} kg de', end=' ')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
