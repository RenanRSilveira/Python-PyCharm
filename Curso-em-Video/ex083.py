ex = str(input('Digite a expressão: '))
lista = list()
for simb in ex:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
print(lista)

if len(lista) == 0:
    print('Expressão válida')
else:
    print('Expressão NÃO é valida')