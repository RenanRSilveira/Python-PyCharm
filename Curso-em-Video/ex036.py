c = float(input('Digite o valor da casa: R$ '))
s = float(input('Qual o salário do comprador: R$ '))
t = int(input('Em quantos anos o comprador pretende pagar? '))
p = c/(t*12)
if p < 0.3 * s:
    print('A prestação será de \033[32mR$ {:.2f}\033[34m\nEmpréstimo aprovado!\033[m'.format(p))
else:
    print('A prestação será de \033[32mR$ {:.2f}\033[31m\nEmpréstimo negado!\033[m'.format(p))