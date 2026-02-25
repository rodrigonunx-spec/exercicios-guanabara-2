print('-' * 50)
print('Bem-vindo à progressão aritmética em Python V.2.0'.center(50))
print('-' * 50)

primeiro = int(input('Digite o primeiro termo da P.A. desejada: ').strip())
razao = int(input('Digite a razão da P.A. desejada: ').strip())
termos = 10
contador = 1

while contador <= termos:
    print(f'{primeiro}', end=' -> ')
    primeiro += razao
    contador += 1
print('Acabou!')
print('Obrigada por utilizar nosso programa de P.A. em Python!'.center(50))