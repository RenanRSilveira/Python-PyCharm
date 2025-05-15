num = int(input('Digite um número de 0 a 9999: '))
n = str(num)
m = num // 1000
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print('Analizando o numero {}'.format(num))
print('Milhar:  {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena:  {}'.format(d))
print('Unidade:  {}'.format(u))