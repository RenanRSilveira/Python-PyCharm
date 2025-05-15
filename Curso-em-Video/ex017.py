from math import sqrt
c = float(input('Digite o valor do primeiro cateto: '))
c2 = float(input('Digite o valor do segundo cateto: '))
h = sqrt((c*c)+(c2*c2))
print('O valor da hipotenusa será de {}'.format(h))