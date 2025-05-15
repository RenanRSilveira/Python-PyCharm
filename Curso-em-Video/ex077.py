lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON')
for p in lista:
    print(f'\nNa palavra {p} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' '),
