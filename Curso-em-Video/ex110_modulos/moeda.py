def metade(p=0, formato=False):
    '''

    :param p: Preço, introduzido no programa principal
    :param formato: Para reduzir o programa e introduzir a nova formatação
    :return: retorna o novo valor e nova formatação
    '''

    n = p * 0.5
    return n if not formato else moeda(n)


def dobro(p=0, formato=False):
    n = 2 * p
    return n if not formato else moeda(n)


def mais(p=0, formato=False):
    n = p * 1.1
    return n if not formato else moeda(n)


def menos(p=0, formato=False):
    n = p * 0.87

    return n if not formato else moeda(n)


def moeda(p=0, moeda='R$ '):
    return f'{moeda}{p:.2f}'.replace('.', ',')

def resumo(p=0):
    print('-'*30)
    print('RESUMO VALOR:'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'A metade é: \t\tR$ {metade(p):.2f}'.replace('.', ','))
    print(f'O dobro é: \t\t\tR$ {dobro(p):.2f}'.replace('.', ','))
    print(f'Aumentando 10%: \tR$ {mais(p):.2f}'.replace('.', ','))
    print(f'Diminuindo 13%: \tR$ {menos(p):.2f}'.replace('.', ','))
    print('-' * 30)
    