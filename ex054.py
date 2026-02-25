from datetime import date
maior_idade = 0
menor_idade = 0

for c in range (1, 8):
    ano = date.today().year
    i = int(input(f'digite o ano de nascimento da {c}ª pessoa: ').strip())
    idade = ano - i
    if idade >= 21:
        maior_idade = maior_idade + 1
    else:
        menor_idade = menor_idade + 1

print(f'Dentre as pessoas acima. {maior_idade} são maiores de idade!')
print(f'E dentre as pessoas acima. {menor_idade} são menores de idade!')