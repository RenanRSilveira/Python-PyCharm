n = int(input('Digite um número: '))
count = 0
for d in range(1, n+1):
    if n % d == 0:
        count += 1
print(f'O número é divisível por {count} termos')
if count == 2:
    print('Primo!')
else:
    print('Não primo!')