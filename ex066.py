print('-' * 50)
print('Bem-vindo ao analisador de números v3.0 em Python!'.center(50))
print('-' * 50)

soma = 0
contador = 0

while True:
    numero = int(input('Digite um número inteiro [999 para parar o programa]: ').strip())
    if numero == 999:
        break
    contador += 1
    soma += numero
    
print(f'Ao todo você digitou {contador} números.')
print(f'A soma de todos os números digitados vale {soma}.')

print('\nObrigada por utilizar o nosso programa analisador em Python!')
print('Por favor, nos dê 5 estrelas, tenha um bom dia e volte sempre!')