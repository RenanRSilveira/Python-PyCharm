def metade(p=0):
    n = p * 0.5
    n = n
    return n


def dobro(p=0):
    n = 2 * p
    return n


def mais(p=0):
    n = p * 1.1
    return n


def menos(p=0):
    n = p * 0.87

    return n


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')