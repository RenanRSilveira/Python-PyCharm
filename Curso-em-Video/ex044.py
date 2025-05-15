v = float(input('Qual o valor do produto: R$ '))
p = str(input('Qual será a condição de pagamento?'
              '\n[1] À vista dinheiro/cheque'
              '\n[2] À vista no cartão'
              '\n[3] 2x no cratão'
              '\n[4] 3x ou mais no cartão\n'))
a = v * 0.9
b = v * 0.95
c = v * 1.2
if p == 1:
    print(f'Você irá pagar R$ {a:.2f}')
elif p == 2:
    print(f'Você irá pagar R$ {b:.2f}')
elif p == 3:
    print(f'Você irá pagar R$ {v:.2f}')
elif p == 4:
    print(f'Você irá pagar R$ {c:.2f}')
else:
    print('Opção inválida!')