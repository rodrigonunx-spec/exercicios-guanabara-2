maior = 0
homem = 0
mulher_20 = 0

while True:
        print('=' * 30)
        print('Cadastre uma pessoa: ')
        print('=' * 30)
        idade = int(input('Digite a idade da pessoa: ').strip())
        sexo = str(input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0])
        while sexo != 'M' and sexo != 'F':
            sexo = str(input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0])
        if idade >= 18:
            maior += 1
        if sexo == 'M':
            homem += 1
        if idade < 20 and sexo == 'F':
            mulher_20 += 1
        print('-=' * 15)
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Gostaria de cadastrar mais pessoas? [S/N]: ').strip().upper()[0])
        print('-=' * 15)
        if continuar == 'N':
            break
print(f'\nAo total no programa, você cadastrou {maior} pessoas maiores de 18 anos!')
print(f'Foram cadastrados {homem} homens no programa!')
print(f'E, foram cadastradas {mulher_20} mulheres menores de 20 anos!')