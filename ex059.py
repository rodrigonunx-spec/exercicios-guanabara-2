from time import sleep
print('-' * 50)
print('Bem-vindo ao menu analisador de números!'.center(50))
print('-' * 50)

menu = 0
n1 = int(input('Digite o valor do primeiro número: ').strip())
n2 = int(input('Digite o valor do segundo número: ').strip())

while menu != 5:
    sleep(1)
    menu = int(input('''Escolha uma ação para ser realizada com os números digitados: 
    [1] Somar os números
    [2] Multiplicar os números
    [3] Verificar qual o maior número
    [4] Digitar novos números
    [5] Sair do programa
    Opção: ''').strip())
    
    if menu == 1:
        print(f'A soma dos números {n1} e {n2} vale {n1 + n2}')
        print('-' * 50)
    elif menu == 2:
        print(f'A Multiplicação dos números {n1} e {n2} vale {n1 * n2}')
        print('-' * 50)
    elif menu == 3:
        if n1 > n2:
            print(f'Comparando os números {n1} e {n2}. O maior entre eles é o número {n1}')
            print('-' * 50)
        else:
            print(f'Comparando os números {n1} e {n2}. O maior entre eles é o número {n2}')
            print('-'  * 50)
    elif menu == 4:
        n1 = int(input('Digite o novo valor do primeiro número: ').strip())
        n2 = int(input('Digite o novo valor do segundo número: ').strip())
    elif menu > 5:
        print('Por favor, digite apenas os números disponíveis no menu de opções!')

print('\nObrigada por utilizar nosso menu analisador de números!')
print('Nos dê um feedback para melhorarmos nosso programa!')
print('Até a próxima!')