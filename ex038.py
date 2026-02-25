print('-' * 100)
print('Bem-vindo ao comparador de números!')
print('Digite dois números inteiros e eu irei falar qual é o maior ou que ambos são iguais!')
print('-' * 100)

a = int(input('Digite o primeiro número: ').strip())
b = int(input('Digite o segundo número: ').strip())

if a > b:
    print(f'O maior número é o primeiro! o número {a} é maior que o número {b}!')
elif a < b:
    print(f'O maior número é o segundo! O número {b} é maior que o número {a}!')
else:
    print(f'Nenhum dos números é maior! O número {a} é o mesmo que o número {b}!')