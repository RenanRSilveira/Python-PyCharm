def contador(i, f, p):
    print(f'Contando de {i} até {f} de {p} em {p}')

    if i < f:
        if p == 0:
            p = 1
        if p < 0:
            p *= -1
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
        print('FIM')
    else:
        if p == 0:
            p = 1
        if p > 0:
            p *= -1
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont += p
        print('FIM')


contador(1, 10, 1)
contador(10, 1, -2)
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

