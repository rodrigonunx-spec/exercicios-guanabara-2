from datetime import date
print('-' * 100)
print('Bem-vindo ao programa de alistamento militar!'.center(100))
print('Aqui você pode descobrir se já passou da hora de se alistar, se está na hora ou se ainda falta um tempo!'.center(100))
print('-' * 100)

pessoa = str(input('Digite se você é homem ou mulher: ').strip().lower())
if pessoa == 'mulher':
    print('Mulheres não precisam se alistar! Mas fique atenta, pois as regras podem mudar no futuro!')
elif pessoa == 'homem': 
    ano_atual = date.today().year
    ano = int(input('Digite o ano que você nasceu: ').strip())
    idade = ano_atual - ano
    atraso = idade - 18
    falta = 18 - idade
    alistamento = ano_atual + falta

    if idade > 18:
        print(f'Já passou da hora de você se alistar! Você já tem {idade}! Seu alistamento foi há {atraso} anos!')
        print(f'Seu alistamento foi no ano de {ano_atual - atraso}!')
    elif idade == 18:
        print(f'Já está na hora de você se alistar no exército! Não deixe para última hora!')
    else:
        print(f'Ainda não está na hora de você se alistar! Mas fique atento! Ainda faltam {falta} anos!')
        print(f'Seu alistamento será no ano de {alistamento}!')
else:
    print('Opção inválida! Por favor, digite "homem" ou "mulher" para continuar!')