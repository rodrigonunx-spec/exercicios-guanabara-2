print('-' * 50)
print('Bem-vindo à Super Tabuada v3.0 em Python!!!'.center(50))
print('-' * 50)

while True:
    numero = int(input('Gostaria de ver a tabuada de qual número? [valores negativos encerram o programa]: ').strip())
    print('-=' * 20)
    if numero < 0:
        break
    for c in range (1, 11):
        print(f'{numero} X {c} = {numero * c}')
    print('-=' * 20)
print('\nObrigado por utilizar nossa Super Calculadora em Python!')
print('Por favor, nos dê 5 estrelas, tenha um bom dia e volte sempre!!')