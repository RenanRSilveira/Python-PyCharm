def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] < 5:
            r['situação'] = 'RUIM'
        elif 5 <= r['média'] < 7:
            r['situação'] = 'RASOÁVEL'
        else:
            r['situação'] = 'BOA'

    return r


# programa principal
resp = notas(6, 4, 5)
print(resp)
