n = int(input('Digite um número: '))
r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
cont = s = 0
cont += 1
s += n
lista = [n]
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    lista += [n]
    cont += 1
    s += n
maior = max(lista)
menor = min(lista)
media = s / cont
print(f'Maior: {maior}')
print(f'Menor: {menor}')
if r == 'N':
    print(f'A soma é {s}')
    print(f'A média é {media}')
    print(f'Você digitou {cont} números')


