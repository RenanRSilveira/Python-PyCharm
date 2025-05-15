'''import math
a = float(input('Digite o valor de um ângulo em graus: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
tg = s/c
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(s,c,tg))'''

from math import radians, sin, cos
a = float(input('Digite o valor de um ângulo em graus: '))
s = sin(radians(a))
c = cos(radians(a))
tg = s/c
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(s, c, tg))