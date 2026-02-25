homem_mais_velho = ''
idade_homem_mais_velho = 0
media_idade = 0
mulheres_menor_de_20 = 0

for c in range (1, 5):
    nome = str(input(f'Digite o nome da {c}° pessoa: ')).strip()
    idade = int(input(f'Digite a idade da {c}° pessoa: ').strip())
    sexo = int(input(f'Qual o sexo da {c}° pessoa. Digite 1 para masculino. 2 para feminino: ').strip())

    if sexo == 1:
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome
    elif sexo == 2:
        if idade < 20:
            mulheres_menor_de_20 = mulheres_menor_de_20 + idade
    if idade > 0:
        media_idade = media_idade + idade
    
print(f'A média de idade do grupo é {media_idade / 4} anos!')
print(f'O homem mais velho se chama: {homem_mais_velho}! E tem {idade_homem_mais_velho} anos!')
print(f'Dentro do grupo nós temos {mulheres_menor_de_20} mulheres que tem menos de 20 anos!')
    