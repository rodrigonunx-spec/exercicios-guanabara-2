s = 0
cont = 0
for c in range (0, 6):
    n = int(input('Digite um número inteiro: ').strip())
    if n % 2 == 0:
        s = s + n
        cont = cont + 1
print(f'A soma somente dos {cont} números pares digitados é: {s}')