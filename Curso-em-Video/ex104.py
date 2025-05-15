def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            print(f'Você digitou o número {valor}')
            return valor
        else:
            print('ERRO!')


n = leiaInt('Digite um número: ')
