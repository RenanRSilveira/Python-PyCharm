while True:
    try:
        n = float(input('Quanto de dinheiro você tem na carteira? R$ '))
        d = n / 4.88
        print('R${:.2f} são exatamente US${:.2f}'.format(n, d))

    except ValueError:
        print('Digite um número válido!')

    else:
        break
