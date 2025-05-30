c = ('\033[m',           # 0  - sem cores
     '\033[0;30;41m'     # 1 - vermelho
     '\033[0;30;42m',    # 2 - verde
     '\033[0;30;43m',    # 3 - amarelo
     '\033[0;30;44m',    # 4 - azul
     '\033[0;30;45m',    # 5 - roxo
     '\033[7;30m',       # 6 - branco
     )


def ajuda(com):
    print(c[1])
    help(com)
    print(c[0], end='')


def titulo(msg):
    tam = len(msg) + 4
    print(c[1], end='')
    print('-'*tam)
    print(f' {msg}')
    print('-'*tam)


# PROGRAMA PRINCIPAL
comando = ''
while True:
    comando = str(input(f'{c[2]}Biblioteca ou Função: '))
    if comando.upper() == 'FIM':
        break

    else:
        ajuda(comando)
titulo('Fim do programa')
