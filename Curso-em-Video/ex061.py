n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = 0
cont = 0
while n < 10:
    n = n + 1
    an = n1 + (n - 1) * r
    cont += 1
    print(f'\033[31m{cont}º\033[m termo = \033[032m{an}\033[m → ', end='')
print('Fim')
