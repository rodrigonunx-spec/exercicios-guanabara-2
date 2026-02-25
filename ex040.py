print('-' * 100)
print('Bem-vindo ao cálculo de média escolar!'.center(100))
print('Digite suas duas notas para ver a sua média e descobrir se passou, de recuperação ou reprovado!'.center(100))
print('-' * 100)

n1 = float(input('Digite sua primeira nota: ').strip())
n2 = float(input('Digite sua segunda nota: ').strip())
media = (n1 + n2) / 2

if n1 > 10 or n2 > 10:
    print('O máximo da nota aceita no sistema é 10! Por favor digite um número dentro do permitido!')
else: 
    if media < 5.0:
        print(f'Você infelizmente tirou apenas {media:.2f} pontos na nota média! \033[1;31mEstá REPROVADO!\033[m')
    elif 5.0 <= media < 7.0:
        print(f'Você infelizmente não foi aprovado, ficou com {media:.2f} pontos na média. \033[1;33mEstá de RECUPERAÇÃO!\033[m')
    else:
        print(f'Parabéns, você passou direto com {media:.2f} pontos na média. \033[1;32mEstá APROVADO!\033[m')

