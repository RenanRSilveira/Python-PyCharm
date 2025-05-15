'''Exercício implementado'''
frase = str(input('Digite uma frase: ')).strip().upper()
n = str(input('Digite a letra que você quer analizar: ')).strip().upper()
print('A letra {} aparece {} vezes'.format(n, frase.count(n)))
print('Aparece pela primeira vez no caractere de numero {}'.format(frase.find(n)+1))
print('Aparece pela ultima vez no caractere de numero {}'.format(frase.rfind(n)+1))

'''Código do exercício original:
nome = str(input('Digite uma frase: ')).strip().upper()
print(nome.count('A'))
print(nome.find('A')+1)
print(nome.rfind('A')+1)
'''