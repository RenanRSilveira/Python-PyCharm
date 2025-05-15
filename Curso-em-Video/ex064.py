n = 0
cont = 0
soma = 0
n = int(input('Digite um valor [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um valor [999 para parar]: '))
print(f'Foram digitados {cont} números!')
print(f'A soma é {soma}')

