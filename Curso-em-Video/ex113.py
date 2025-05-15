def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        else:
            print(f'Você digitou o número {n}')
            break


def leiaFloat(msg):
    while True:
        try:
            m = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número real válido!\033[m')
        else:
            print(f'Você digitou o número {m}')
            break


n = leiaInt('Digite um número inteiro: ')
m = leiaFloat('Digite um número real: ')