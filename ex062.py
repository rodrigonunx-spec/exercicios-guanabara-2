print('-' * 50)
print('Bem-vindo à Super Progressão Aritmética em Python v3.0!'.center(50))
print('-' * 50)

numero = int(input('Digite o primeiro termo da P.A.: ').strip())
razao = int(input('Digite a razão da P.A.: ').strip())
contador = 1
termos = 10
termos_adicionais = 1
a = numero 

while termos_adicionais > 0:
    while contador <= termos:
        print(f'{numero}', end=' -> ')
        numero += razao
        contador += 1
    print('Pausa...')
    termos_adicionais = int(input('Gostaria de ver mais quantos termos da mesma P.A.: ').strip())
    termos += termos_adicionais
else:
    print('ACABOU!!!')
    print(f'Você visualizou {contador - 1} números na P.A. cujo primeiro termo foi o número {a}, o último termo foi o número {numero - razao} e a razão o número {razao}.')
print('\nObrigado por utilizar nosso código de super progressão aritmética.')
print('Volte sempre e nos dê 5 estrelas!')