print('-' * 50)
print('Bem-vindo ao analisador de números em Python!'.center(50))
print('-' * 50)

soma = 0
contador = 0
numeros = int(input('Digite um número inteiro. [digite 999 caso queira parar o programa]: ').strip())

while numeros != 999:
    soma += numeros
    contador += 1
    numeros = int(input('Digite um número inteiro. [digite 999 caso queira parar o programa]: ').strip())
print('ACABOU!')
print(f'Você analisou {contador} números em nosso programa em Python!')
print(f'A soma de todos os números digitados é igual a {soma}!')
print('\nObrigada por utilizar nosso programa analisador de números em Python!')
print('Por favor, nos dê 5 estrelas, tenha um bom dia e volte sempre!')