soma = 0
count = 0
for c in range(3, 499, 3):
    if c % 2 != 0:
        print(c)
        soma += c
        count += 1
print(f'Foram digitados {count} termos e o somatório deles é {soma}')