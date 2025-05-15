lista = ('Palmeiras', 'Grêmio', 'Atlético', 'Flamengo', 'Botafogo',
'Bragantino', 'Fluminense', 'Athletico', 'Internacional', 'Fortaleza',
'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia','Santos', 'Goiás',
'Coritiba', 'América-MG')
print(f'Os 5 primeiros colocados são: {lista[0:5]}')
print(f'Os 4 rebaixados são: {lista[16:21]}')
print(f'Em ordem albabética: {sorted(lista)}')
a = str(input('Digite o time que você deseja saber a posição: ')).strip().capitalize()
if a == 'São paulo':
    print('O São Paulo está na 11ª posião')
else:
    print(f'{a} está na {lista.index(a)+1}ª posição')