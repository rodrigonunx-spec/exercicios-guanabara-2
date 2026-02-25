print('=' * 40)
print('Boas vindas ao banco Xavier!'.center(40))
print('=' * 40)

sacar = int(input('Boa tarde. Qual valor deseja sacar da sua conta: ').strip())
while True:
    cedula_50 = sacar // 50
    cedula_20 = sacar % 50 // 20
    cedula_10 = sacar % 50 % 20 // 10
    cedula_1 = sacar % 50 % 20 % 10 // 1
    print('-=' * 20)
    print(f'Você efetuou um saque no valor de R${sacar:.2f}')
    print(f'''Total de R${cedula_50} cédulas de R$50.00
Total de R${cedula_20} cédulas de R$20.00
Total de R${cedula_10} cédulas de R$ 10.00
Total de R${cedula_1} cédulas de R$1.00''')
    print('-=' * 20)
    continuar = str(input('Gostaria de efetuar mais algum saque? [S/N]: ').strip().upper()[0])
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Gostaria de efetuar mais algum saque? [S/N]: ').strip().upper()[0])
    if continuar == 'S':
        sacar_mais = int(input('Digite o valor que deseja sacar a mais: ').strip())
        sacar += sacar_mais
    else:
        break

print('Agradecemos pela sua confiança no Banco Xavier!!')
print('Tenha um bom dia e volte sempre!!')