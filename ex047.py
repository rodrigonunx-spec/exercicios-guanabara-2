print('Os números pares entre 1 e 50 são: ')
for c in range (1, 51):
    if c % 2 == 0:
        print(c, end=' ')

print('\nOs números ímpares entre 1 e 50 são: ')
for c in range (1, 51):
    if c % 2 == 1:
        print(c, end=' ')

#----------------------------------------------------------------------------

print('\nOs números pares entre 1 e 50 são:')
for c in range (2, 51, 2):
    print(c, end=' ')

print('\nOs números ímpares entre 1 e 50 são: ')
for c in range (1, 51, 2):
    print(c, end=' ')
