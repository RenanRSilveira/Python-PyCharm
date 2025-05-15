ci = cs = cm = 0
while True:
    i = int(input('Digite a idade: '))
    s = ' '
    while s not in 'FM':
        s = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    if i > 17:
        ci += 1
    if s == 'M':
        cs += 1
    if s == 'F' and i < 21:
        cm += 1
    p = ' '
    while p not in 'SN':
        p = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if p == 'N':
        break
print(f'{ci} pessoas tem mais de 18 anos\n{cs} homens cadastrados\n{cm} mulheres com menos de 20 anos')