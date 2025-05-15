from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(n)
o = sorted(n)
print(f'Menor: {o[0]}\nMaior: {o[4]}')