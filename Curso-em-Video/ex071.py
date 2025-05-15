print('-'*30)
print('Banco CEV')
print('-'*30)
from math import floor
v = int(input('Qual valor você quer sacar? R$ '))
c = floor(v / 50)
c1 = v % 50
vi = floor(c1 / 20)
vi1 = c1 % 20
d = floor(vi1 / 10)
u = vi1 % 10
if c > 0:
    print(f'Total de {c} cédulas de R$50,00')
if vi > 0:
    print(f'Total de {vi} cédulas de R$20,00')
if d > 0:
    print(f'Total de {d} cédulas de R$10,00')
if u > 0:
    print(f'Total de {u} cédulas de R$1,00')
