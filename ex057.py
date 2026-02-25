nome = str(input('Digite o nome da criança: ').strip())

sexo = str(input('Digite o sexo da criança (M/F): ').strip().upper())[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados invalidos. Por favor, informe o sexo da criança (M/F): ').strip().upper())[0]
    if sexo == 'M':
        print(f'A criança foi registrada com o nome {nome} e sexo Masculino')
    if sexo == 'F':
        print(f'A criança foi registrada com o nome {nome} e sexo Feminino')