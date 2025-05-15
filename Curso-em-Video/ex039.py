a = int(input('Digite o ano de nascimento: '))
t = 2023 - a
b = 18 - t
c = t - 18
if t < 18:
    if b == 1:
        print('\033[34mVocê não precisa se alistar, falta {} ano\nVocê deverá se alistar em \033[31m{}!'.format(b, a+18))
    else:
        print('\033[34mVocê não precisa se alistar, faltam {} anos\nVocê deverá se alistar em\033[31m {}!'.format(b, a+18))
elif t > 18:
    if c == 1:
        print('\033[31mJá passou da hora de se alistar, você está atrasado em {} ano.'
          '\nVocê deveria ter se alistado em\033[34m {}!'.format(c, a + 18))
    else:
        print('\033[31mJá passou da hora de se alistar, você está atrasado em {} anos.'
          '\nVocê deveria ter se alistado em \033[34m{}!'.format(c, a + 18))
else:
    print('\033[32mEstá na hora de se alistar!')