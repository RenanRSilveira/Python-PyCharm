a = int(input('Digite um valor inteiro: '))
b = int(input('Digite outro valor inteiro: '))
if a > b:
    print('{} é maior que {}'.format(a, b))
elif b > a:
    print('{} é maior que {}'.format(b, a))
else:
    print('Os valores são iguais')