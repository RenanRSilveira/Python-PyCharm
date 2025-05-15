d = float(input('Digite a distância da viagem em km: '))
if d <= 200:
    v = d * 0.5
else:
    v = d * 0.45
print('O valor da passagem será de \033[32mR$ {:.2f}'.format(v))