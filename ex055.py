maior = 0
menor = 10000

for c in range (1, 6):
    peso = float(input(f'Digite o peso da {c}° pessoa em KG: ').strip())
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'A pessoa com maior peso pesa: {maior:.2f} KG!')
print(f'A pessoa com menor peso pesa: {menor:.2f} KG!')

print('Segundo metodo do Guanabara: ')
maior = 0
menor = 0

print('-' * 50)
print('bem-vindo ao comparador de pesos em python!'.center(50).title())
print('-' * 50)

for c in range (1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: ').strip())
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'A pessoa com o maior peso digitado foi a pessoa com {maior}KG!')
print(f'A pessoa com o menor peso digitado foi a pessoa com {menor}KG!')