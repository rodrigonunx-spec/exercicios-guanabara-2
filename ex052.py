from math import sqrt
print('Analisador de números primos!')

n = int(input('Digite um número para verificar se ele é primo: ').strip())
lim = int(sqrt(n)) + 1

if n < 2:
    print('Números menores que  2, NÃO SÃO PRIMOS!')
elif n == 2:
    print('O número 2 é o ÚNICO número que é PAR e PRIMO!')
elif n % 2 == 0:
    print('NENHUM número par, COM EXCESSÃO DO 2, é primo!')
else: 

    for c in range (3, lim, 2):
        if n % c == 0:
            print(f'O número {n}, NÃO É PRIMO!')
            break
    else:
        print(f'O número {n}, É PRIMO!')

print('-' * 100)

print('Método tradicional, verificando a quantidade de divisores!')

print('-' * 50)
print('bem-vindo ao analisador de números primos em python!'.center(50).title())
print('-' * 50)

n = int(input('\033[mDigite um número para verificar se ele é primo: ').strip())
total = 0

for c in range (1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')

if total > 2:
    print(f'\n\033[mO número {n} foi divisível por {total} números! Portanto NÃO É PRIMO!')
else:
    print(f'\n\033[mO número {n} foi divisível por {total} números! Portanto, É PRIMO!')
print('-' * 100)