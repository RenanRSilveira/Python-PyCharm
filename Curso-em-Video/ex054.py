from datetime import date
hoje = date.today().year
count = 0
cont = 0

for a in range(1, 8):
    ano = int(input('Digite seu ano de nascimento: '))
    i = hoje - ano
    if i < 18:
       count += 1
    elif i > 17:
       cont += 1

if count < 2:
    print(f'{count} pessoa não atingiu a maior idade')
else:
    print(f'{count} pessoas não atingiram a maior idade')
if cont > 2:
    print(f'{cont} pessoas já atingiram a maior idade')
else:
    print(f'{cont} pessoa não atingiu a maior idade')