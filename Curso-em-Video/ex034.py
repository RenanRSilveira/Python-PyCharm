s = float(input('Digite o valor do salário: '))
if s > 1250:
    a = s * 1.1
else:
    a = s * 1.15
print('O novo salário será de \033[1;32m{:.2f}'.format(a))