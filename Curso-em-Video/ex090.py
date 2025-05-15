aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['nota'] = float(input('Nota: '))
if aluno['nota'] >= 7:
    aluno['Situação'] = ('Aprovado')
elif aluno['nota'] < 6 and aluno['nota'] >= 5:
    aluno['Situação'] = ('Recuperação')
else:
    aluno['Situação'] = ('Reprovado')
for k, v in aluno.items():
    print(f'{k} é {v}')