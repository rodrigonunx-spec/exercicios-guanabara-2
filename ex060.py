print('-' * 50)
print('Bem-vindo ao cálculo de fatorial em Python com WHILE!'.center(50))
print('-' * 50)

n = int(input('Digite o número que deseja ver o fatorial: ').strip()) #O usuário digita um número e o programa cálcula seu fatorial.
fatorial = 1 #Como o fatorial é uma multiplicação, se começasse com 0, seria sempre 0.
contador = n #O contador vai receber o número digitado menos 1, assim ele multiplica o fatorial que é um acumulador.

print(f'Calculando {n}! =', end=' ') #caso estivesse dentro do while, ele printaria a frase a cada loop, o que não é necessário, então ele fica fora do while.
while contador > 0:
    print(f'{contador} ', end=' ')
    print('X ' if contador > 1 else '= ', end=' ') #O print acima é para mostrar a multiplicação, ele printa o número do contador, depois um 'X' se o contador for maior que 1, ou um '=' se for igual a 1, e o end=' ' é para não quebrar a linha.
    fatorial *= contador #O fatorial é multiplicado pelo contador, que vai diminuindo a cada loop, até chegar em 1, quando o contador for 0, o loop para e o fatorial já estará calculado.
    contador -= 1 #O contador é decrementado a cada loop, até chegar em 0, quando o loop termina.
print(f'{fatorial}')

#--------------------------------------------------------------------------------

print('-' * 50)
print('Bem-vindo ao cálculo de fatorial em Python com FOR!')
print('-' * 50)

numero = int(input('Digite o número que deseja ver o fatorial: ').strip())
fatorial = 1

print(f'Calculando {numero}! =', end=' ')
for c in range (numero, 0, -1):
    print(f'{c}', end=' ')
    print('X' if c > 1 else '=', end=' ')
    fatorial *= c
print(f'{fatorial}')