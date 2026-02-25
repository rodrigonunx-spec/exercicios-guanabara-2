print('-' * 50)
print('Bem-vindo ao contador de números em Python v2.0'.center(50))
print('-' * 50)

continuar = 'S'
maior = 0
menor = 0
media = 0
contador = 0

while continuar == 'S':
    numero = int(input('Digite um número inteiro: ').strip())
    if contador == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    media += numero
    contador += 1
    continuar = str(input('Gostaria de continuar a digitar números? Digite S para sim ou N para não: ').strip().upper()[0])
print(f'Você digitou {contador} números. Entre eles o menor foi o número {menor} e o maior foi o número {maior}')
print(f'A média entre os números digitados é de {media / contador}')

print('\nObrigada por utilizar o nosso programa analisador de números em Python v2.0')
print('Por favor, nos dê 5 estrelas, tenha um bom dia e volte sempre!')