print('-' * 50)
print('Bem-vindo à calculadora de IMC em Python!')
print('-' * 50)

peso = float(input('Digite o valor do seu peso em KG: ').strip())
altura = float(input('Digite sua altura em Metros! ').strip())
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC foi de {imc:.2f}. Portanto está abaixo do peso!')
elif 18.5 <= imc < 25:
    print(f'Seu IMC foi de {imc:.2f}. Portanto está no peso ideal!')
elif 25 <= imc < 30:
    print(f'Seu IMC foi de {imc:.2f}. Portanto está sobrepeso!')
elif 30 <= imc < 40:
    print(f'Seu IMC foi de {imc:.2f}. Portanto está em obesidade!')
else:
    print(f'Seu IMC foi de {imc:.2f}. Portanto está em obesidade mórbida!')