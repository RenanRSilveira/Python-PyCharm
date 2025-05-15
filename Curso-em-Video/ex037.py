n = int(input('Digite um número inteiro: '))
c = int(input('Você quer que esse número seja convertido para qual base?'
              '\nDigite 1 para binário\nDigite 2 para octal\nDigite 3 para hexadecimal\n'))
if c == 1:
    print('{} em binário é {}'.format(n, bin(n)))
elif c == 2:
    print('{} em octal é {}'.format(n, oct(n)))
elif c == 3:
    print('{} em hexadecimal é {}'.format(n, hex(n)))
else:
    print('Opção inválida!')
