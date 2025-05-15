from datetime import date
h = date.today().year
a = int(input('Digite o ano de nascimento do atleta: '))
i = h - a
if i < 10 and i > 1:
    print(f'O atleta tem {i} anos\nCategoria \033[34mMirim')
elif i > 9 and i < 15:
    print(f'O atleta tem {i} anos\nCategoria \033[34mInfantil')
elif i > 15 and i < 20:
    print(f'O atleta tem {i} anos\nCategoria \033[34mJunior')
elif i > 19 and i < 26:
    print(f'O atleta tem {i} anos\nCategoria \033[34mSênior')
elif i > 25 and i < 105:
    print(f'O atleta tem {i} anos\nCategoria \033[34Master')
else:
    print('A pessoa não pode participar')