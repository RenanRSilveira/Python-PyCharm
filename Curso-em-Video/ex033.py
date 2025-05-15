'''a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite outro número inteiro: '))
lista = [a, b, c]
print(max(lista))
print(min(lista))'''

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite outro número inteiro: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número é: \033[31m{}\033[m'.format(menor))
maior = b
if c > a and c > b:
    maior = c
if a > b and a > c:\
    maior = a
print('O maior número é: \033[32m{}'.format(maior))
