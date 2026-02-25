print('-' * 100)
print('Bem-vindo ao analisador de triângulos V2.0!')
print('Agora, além de falarmos se suas retas podem formar um triângulo, ainda falaremos qual triângulo formaria!')
print('-' * 100)

a = float(input('Digite o valor da primeira reta: ').strip())
b = float(input('Digite o valor da segunda reta: ').strip())
c = float(input('Digite o valor da terceira reta: ').strip())

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos de reta acima PODEM formar um triângulo!')
    if a == b and a == c and b == c:
        print('Os segmentos de reta acima formam um triângulo equilátero!')
    elif a != b and a != c and b != c:
        print('Os segmentos de reta acima formam um triângulo escaleno!')
    elif a != b or a != c or b != c:
        print('Os segmentos de reta acima formam um triângulo isoceles!')
else:
    print('Os segmentos de reta acima NÃO PODEM formar um triângulo!')

        