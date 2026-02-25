s = 0
print('A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é: ')
for c in range (1, 501, 2):
    if c % 3 == 0:
        s = s + c
print(s)