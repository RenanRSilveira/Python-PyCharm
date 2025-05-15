m = float(input('Digite seu peso em kg: '))
h = float(input('Digite sua altura em metros: '))
imc = m / (h*h)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}, você está abaixo do peso!')
elif imc < 25.1:
    print(f'Seu IMC é {imc:.2f}, você está com o peso ideal!')
elif imc < 30.1:
    print(f'Seu IMC é {imc:.2f}, você está com sobrepeso!')
elif imc < 40.1:
    print(f'Seu IMC é {imc:.2f}, você está com obesidade!')
else:
    print(f'Seu IMC é {imc:.2f}, você está com obesidade mórbida!')