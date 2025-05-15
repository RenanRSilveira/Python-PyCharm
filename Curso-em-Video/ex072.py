ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número de 0 a 20 '))
while n < 0 or n > 20:
    n = int(input('Digite um número de 0 a 20 '))
print(f'Você digitou o número \033[31m{ext[n]}')
