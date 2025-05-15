n = (int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3)+1}')
else:
    print('O número 3 não apareceu na lista')
print('Os valores pares digitados foram ', end='')
for p in n:
    if p % 2 == 0:
        print(p, end=' ')

