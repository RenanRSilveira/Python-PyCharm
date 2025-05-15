cont = tot = menor = contp = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: ')).capitalize().strip()
    p = float(input('Digite o preço do produto: R$ '))
    contp += 1
    if contp == 1:
        menor = p
        barato = nome
    else:
        if p < menor:
            menor = p
            barato = nome
    if p > 999:
        cont += 1
    tot += p
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if c == 'N':
        break
print(f'O total da compra foi {tot}')
print(f'O produto mais barato foi {barato} que custa {menor}')
if cont == 1:
    print(f'Temos {cont} produto custando mais de R$1000.00')
else:
    print(f'Temos {cont} produtos custando mais de R$1000.00')
