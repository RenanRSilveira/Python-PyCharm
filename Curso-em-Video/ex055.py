lista = []
for c in range(1, 6):
    p = float(input('Digite o peso em kg: '))
    lista += [p]
lista.sort()
maior = lista[4]
menor = lista[0]
print(f'\033[33mO maior peso é \033[31m{maior}\033[33m kg e o menor \033[31m{menor}\033[33m kg')
