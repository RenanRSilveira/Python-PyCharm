from datetime import date
hoje = date.today().year
listanome = []
maisvelho = 0
somaidade = 0
contm = 0
for c in range(1, 5):
    nome = str(input(f'Digite o nome da {c}ª pessoa: ')).capitalize()
    listanome += nome
    nasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = hoje - nasc
    somaidade += idade
    media = somaidade / c
    sexo = int(input(f'Qual o sexo da {c}ª pessoa?\nDigite [1] para masculino e [2] para feminino: '))
    if sexo == 2 and idade < 20:
        contm += 1
    if sexo == 1 and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
print(f'O homem mais velho se chama \033[31m{nomevelho}\033[m')
print(f'A média de idade é \033[31m{media:.2f}\033[m anos')
print(f'\033[31m{contm}\03a3[m mulheres tem menos de 20 anos')

