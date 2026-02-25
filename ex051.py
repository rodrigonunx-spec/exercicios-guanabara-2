print('Bem-vindo à progressão aritmética em Python!')

a = int(input('Digite o primeiro termo da PA: ').strip())
r = int(input('Digite a razão da PA: ').strip())

for c in range (0, 10):
    pa = (a + (c * r))
    print(pa, end=' -> ')
print('FIM')