def metade(p=0, formato=False):
    '''

    :param p: Preço, introduzido no programa principal
    :param formato: Para reduzir o programa e introduzir a nova formatação
    :return: retorna o novo valor e nova formatação
    '''

    n = p * 0.5
    return n if formato is False else moeda(n)


def dobro(p=0, formato=False):
    n = 2 * p
    return n if formato is False else moeda(n)


def mais(p=0, formato=False):
    n = p * 1.1
    return n if not formato else moeda(n)


def menos(p=0, formato=False):
    n = p * 0.87

    return n if not formato else moeda(n)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')
