from random import randint
from time import sleep
n = int(input('Digite um número entre 0 e 5: '))
a = randint(0, 5)
print('Aguarde o resultado em \033[31m2\033[m segundos')
sleep(1)
print('Aguarde o resultado em \033[31m1\033[m segundo')
sleep(1)
print('Pensei no número \033[32m{}'.format(a))
if n == a:
    print('Números iguais!')
else:
    print('\033[31mNúmeros diferentes!')