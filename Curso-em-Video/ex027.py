nome = str(input('Digite o nome da pessoa: ')).upper().strip()
n = nome.split()
print('Primeiro nome: \033[36m{}\033[m'.format(n[0].capitalize()))
print('Ultimo nome: \033[36m{}'.format(n[-1].capitalize()))