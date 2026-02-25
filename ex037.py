print('-' * 100)
print('Bem-vindo ao conversor de bases em Python!')
print('Digite um número decimal qualquer e descubra o seu valor em binário, octal ou hexadecimal!')
print('-' * 100)

d = int(input('Digite um número inteiro decimal: ').strip())

print('Digite 1 para binário!')
print('Digite 2 para octal!')
print('Digite 3 para hexadecimal!')
conversor = int(input('Digite para qual base gostaria de converter o número decimal escolhido: ').strip())

b = bin(d)
o = oct(d)
h = hex(d)

if conversor == 1:
    print(f'O número decimal {d} em binário é {b[2:]}')
elif conversor == 2:
    print(f'O número decimal {d} em octal é {o[2:]}')
elif conversor == 3:
    print(f'O número decimal {d} em hexadecimal é {h[2:]}')
else:
    print('Número inválido! Por favor escolha apenas os números acima!')