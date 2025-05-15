n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = 0
lista = [n1, n2]
while op != 5:
    print('''O que você deseja fazer com esses números?
[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa''')
    op = int(input('Sua opção: '))
    if op == 1:
        r = n1 + n2
        print(r)
    elif op == 2:
        r = n1 * n2
        print(r)
    elif op == 3:
        if n1 > n2:
            print(f'Maior: {n1}\nMenor: {n2}')
        elif n2 > n1:
            print(f'Maior: {n2}\nMenor: {n1}')
        else:
            print('Números iguais')
    elif op == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif op == 5:
        print('Fim')
