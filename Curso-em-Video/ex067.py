while True:
    print('Para interromper o programa, basta digitar um número negativo!')
    n = int(input('Digite um número para saber sua tabuada: '))
    if n < 0:
        break
    for a in range(1, 11):
        m = a * n
        print(f'{n} x {a} = {m}')
print('Programa encerrado!')