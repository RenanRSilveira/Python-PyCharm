galera = []
pessoa = {}
idade = []
tidade = 0
muleres = []
acmedia = []
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
    if pessoa['sexo'] == 'F':
        muleres.append(pessoa['nome'])

    pessoa['idade'] = int(input('Idade: '))
    tidade += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
media = tidade / len(galera)

print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
print(f'B) A média de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
print(muleres)
print('D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
