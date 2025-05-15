n = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n + n2) / 2
if m < 5:
    print(f'Sua média é {m:.2f}\n\033[31mREPROVADO!')
elif m >= 5 and m < 7:
    print(f'Sua média é {m:.2f}\n\033[33mRECUPERAÇÃO!')
else:
    print(f'Sua média é {m:.2f}\n\033[32mAPROVADO!')