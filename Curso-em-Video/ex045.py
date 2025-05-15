from random import choice
from time import sleep
j = int(input('''[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA\nDigite sua opção: '''))
lista = [1, 2, 3]
c = choice(lista)
if j == 1:
    print('Você escolheu \033[34mPEDRA\033[m')
    sleep(1)
    if c == 2:
        print('O computador escolheu PAPEL, você \033[31mperdeu!')
    elif c == 3:
        print('O computador escolheu TESOURA, você \033[32mvenceu!')
    else:
        print('O computador escolheu PEDRA, jogo \033[33mempatado!')
if j == 2:
    print('Você escolheu \033[34mPAPEL\033[m')
    sleep(1)
    if c == 1:
        print('O computador escolheu PEDRA, você \033[32mvenceu!')
    elif c == 3:
        print('O computador escolheu TESOURA, você \033[31mperdeu!')
    else:
        print('O computador escolheu PAPEL, jogo \033[33mempatado!')
if j == 3:
    print('Você escolheu \033[34mTESOURA\033[m')
    sleep(1)
    if c == 2:
        print('O computador escolheu PAPEL, você \033[32mvenceu!')
    elif c == 3:
        print('O computador escolheu TESOURA, jogo \033[33mempatado!')
    else:
        print('O computador escolheu PEDRA, jogo você \033[31mperdeu!')
