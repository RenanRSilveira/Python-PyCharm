print('MENU PRINCIPAL'.center(30))
print('-' * 30)

from ex115a import options

try:
    options

except ValueError:
    print('ERRO: por favor, digite um numero inteiro válido')

