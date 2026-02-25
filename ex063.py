print('-' * 50)
print('Bem-vindo ao gerador da sequência de Fibonacci em Python'.center(50))
print('-' * 50)

a1 = 0
a2 = 1
contador = 3
numero = int(input('Digite quantos números da sequência de Fibonacci gostaria de visualizar: ').strip())

print(f'{a1}', end=' -> ')
print(f'{a2}', end=' -> ')
while contador <= numero:
    a3 = a1 + a2
    print(f'{a3}', end=' -> ')
    a1 = a2
    a2 = a3
    contador +=1
print('FIM!')
print(f'\nVocê visualizou {numero} números da sequência de Fibonacci!')
print('Obrigada por utilizar nosso programa!')
print('Por favor nos dê 5 estrelas, tenha um bom dia e volte sempre!')