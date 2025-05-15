from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] == 0:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    dados['ano'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano'] + 35) - datetime.now().year)

    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
