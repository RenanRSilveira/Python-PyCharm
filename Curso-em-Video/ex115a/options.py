from ex115a import Menu

while True:
    print(Menu.txt)
    op = int(input('Sua opção: '))
    print('-' * 30)

    if op < 1 or op > 3:
        print('-' * 30, end='')
        print('\033[31m')
        print('OPÇÃO INVÁLIDA'.center(30))
        print('\033[m', end='')
        print('-' * 30)
        print(Menu.txt)
        op = int(input('Sua opção: '))
    if op == 1:
        print('Opção 1'.center(30))
        print('-' * 30)
    elif op == 2:
        print('Opção 2'.center(30))
        print('-' * 30)
    elif op == 3:
        print('Saindo do sistema... Até logo!')
        break