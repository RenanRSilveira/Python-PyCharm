v = int(input('Digite a velocidade do carro em km/h: '))
print('A velocidade limite é de \033[4;34m80km/h!\033[m')
m = (v-80)*7
if v > 80:
    print('O condutor foi multado em \033[32mR$ {},OO'.format(m))
else:
    print('O condutor \033[031mnão\033[m será multado')