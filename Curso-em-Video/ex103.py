def ficha(nome, gols):

    print(f'O jogador {nome} fez {gols} gols')


n = str(input('Nome: ')).strip().capitalize()
g = str(input('Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.isalpha():
    n = str(n)
else:
    n = '<desconhecido>'

ficha(n, g)
