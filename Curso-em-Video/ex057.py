M = 0
F = 0
sexo = 0
sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite o seu sexo [M/F]: ')).upper().strip()
if sexo == 'F':
    print('Feminino')
else:
    print('Masculino')
