l = float(input('Largura da parede em metros: '))
h = float(input('Altura da parede em metros: '))
a = l * h
x = a / 2
print('Sua parede tem a dimensão de {:.2f}m x {:.2f}m e sua área é de {:.2f}m²'.format(l, h, a))
print('Você precisará de {:.3f} litros de tinta'.format(x))