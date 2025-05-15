from ex108_modulos import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.mais(p))}')
print(f'Reduzindo 13% de {moeda.moeda(p)} é {moeda.moeda(moeda.menos(p))}')