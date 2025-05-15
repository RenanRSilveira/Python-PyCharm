from random import randint
pc = randint(0, 10)
p = int(input('Digite um número de 0 a 10: '))
count = 1
while pc != p:
    print(f'O computador pensou no número {pc}')
    pc = randint(0, 10)
    p = int(input('Digite um número de 0 a 10: '))
    count += 1
if pc == p:
    print(f'O computador pensou no número {pc} e você {p}! \033[032mNúmeros iguais!')
    if count > 1:
        print(f'Precisou de {count} tentativas!')
    else:
        print('Precisou de 1 tentativa!')