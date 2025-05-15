r = int(input('Digite a razão da PA: '))
a1 = int(input('Digite o primeiro termo da PA: '))
for n in range(1, 11):
    an = a1 + (n - 1)*r
    print(an, end='  ')