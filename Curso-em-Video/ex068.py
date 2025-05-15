from random import randint
cont = 0
while True:
    n = int(input('Digite um número: '))
    pc = randint(1, 10)
    tot = n + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {n} e o computador {pc}. Total {tot}')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Vamos jogar novamente!')
            cont += 1
        else:
            break
    elif tipo == 'I':
        if tot % 2 != 0:
            print('Vamos jogar novamente!')
            cont += 1
        else:
            break
print(f'GAME OVER!Você jogou {cont} vezes!')