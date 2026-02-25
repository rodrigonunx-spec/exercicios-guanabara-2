from datetime import date

print('-' * 100)
print('Bem-vindo ao cadastro de atletas!')
print('Digite o ano de nascimento do atleta para saber sua categoria!')
print('-' * 100)

nascimento = int(input('Digite seu ano de nascimento: ').strip())
ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print(f'Você tem {idade} anos. Portanto você se encaixa nos atletas MIRIM!')
elif 9 < idade <= 14:
    print(f'Você tem {idade} anos. Portanto você se encaixa nos atletas INFANTIL!')
elif 14 < idade <= 19:
    print(f'Você tem {idade} anos. Portanto você se encaixa nos atletas JÚNIOR!')
elif 19 < idade <= 25:
    print(f'Você tem {idade} anos. Portanto você se encaixa nos atletas SÊNIOR!')
else:
    print(f'Você tem {idade} anos. Portanto você se encaixa nos atletas MASTER!')