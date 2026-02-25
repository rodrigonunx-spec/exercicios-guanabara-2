print('-' * 50)
print('Bem-vindo ao detector de palíndromos em Python!')
print('-' * 50)

frase = str(input('Digite uma frase aleatória. Por Favor, desconsidere acentos: ')).strip().replace(' ', '').lower()
for c in range (1):
    invertido = frase [::-1]
    if invertido != frase:
        print(invertido)
        print(f'A frase digitada de forma invertida fica {invertido}! Portanto, não é um palíndromo!')
    else:
        print(f'A frase digitada de forma invertida fica {invertido}! Portanto, é um palíndromo!')

print('\n\nSegundo Método:')
print('-' * 50)
frase = str(input('digite uma frase: '))
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('A frase é um palíndromo!')
else: 
    print('A frase não é um palíndromo!')
print('-' * 50)