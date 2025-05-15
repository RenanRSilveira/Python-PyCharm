def idade(n):
    from datetime import datetime
    hj = datetime.now().year
    i = hj - n
    if i < 16:
        return f'Você tem {i} anos e o voto é proibido!'
    elif 15 < i < 18 or i > 65:
        return f'Você tem {i} anos e o voto é opcional'
    else:
        return f'Você tem {i} anos e o voto é OBRIGATÓRIO'


a = int(input('Em que ano você nasceu? '))
print(idade(a))
