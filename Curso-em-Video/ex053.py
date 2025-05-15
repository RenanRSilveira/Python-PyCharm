print('\033[32mBem vindo! Este é um programa que detecta palíndromos!\033[m')
frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
contrario = frase[::-1]
print(f'Sua frase ao contrário é {contrario}')
if frase == contrario:
    print('Essa frase \033[32mé\033[m um palíndomo!')
else:
    print('Essa frase \033[31mnão\033[m é um palíndromo')
    
'''frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    print(junto[letra], end='')
    inverso += junto[letra]
if inverso == junto:
    print('\nÉ um palíndromo')
else:
        print('\nNão é um palíndromo')'''