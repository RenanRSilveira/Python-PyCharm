a = float(input('Digite o valor da primeira aresta: '))
b = float(input('Digite o valor da segunda aresta: '))
c = float(input('Digite o valor da terceira aresta: '))
if a + b > c and a + c > b and c + b > a:
    print('\033[0;32mForma\033[m um triângulo')
else:
    print('\033[0;31mNão\033[m forma um triângulo')