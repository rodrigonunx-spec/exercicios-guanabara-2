print('Bem-vindo à tabuada em Python!')
n = int(input('Digite um número qualquer para ver sua tabuada: ').strip())
print('-' * 23)
print(f'Tabuada do número {n}:')
for c in range(1, 11):
    print(f'{n} * {c} = {n * c}')
print('-' * 23)