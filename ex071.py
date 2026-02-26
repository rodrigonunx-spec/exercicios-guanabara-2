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
    if cedula_50 > 0:
        print(f'Total de {cedula_50} cédulas de \033[31mR$50.00\033[m')
    if cedula_20 > 0:
        print(f'Total de {cedula_20} cédulas de \033[33mR$20.00\033[m')
    if cedula_10 > 0:
        print(f'Total de {cedula_10} cédulas de \033[34mR$10.00\033[m')
    if cedula_1 > 0:
        print(f'Total de {cedula_1} cédulas de \033[32mR$1.00\033[m')
    print('-=' * 20)
    break
    
print('\nAgradecemos pela sua confiança no Banco Xavier!!')
print('Tenha um bom dia e volte sempre!!')
