listanum = []
for n in range(0, 5):
    listanum.append(int(input('Digite um número: ')))

maior = max(listanum)
menor = min(listanum)
print(f'O maior valor digitado foi {maior}', end=' ')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'na posição {i}')
print(f'O menor valor digitado foi {menor}', end=' ')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'na posição {i}')