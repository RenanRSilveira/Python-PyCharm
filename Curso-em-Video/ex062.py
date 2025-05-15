n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = n1
cont = 1
total = 0
m = 10
while m != 0:
    total = total + m
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += r
        cont += 1
    print('Pausa')
    m = int(input('Quantos termos a mais você quer ver? '))
print('Fim')


