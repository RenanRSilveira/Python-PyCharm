def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        else:
            return n



def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL'.center(42))
    c = 1
    for item in lista:
        print(f'\033[33m{c} -\033[36m {item}\033[m')
        c += 1
    print(linha())
    op = leiaInt('Sua opção: ')
    return op
