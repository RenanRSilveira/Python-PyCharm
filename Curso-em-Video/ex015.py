t = int(input('Quantos dias o carro ficou algado? '))
d = float(input('Quanto km foram rodados? '))
v = (60 * t) + (0.15 * d)
print('O valor a ser pago é de R${}'.format(v))