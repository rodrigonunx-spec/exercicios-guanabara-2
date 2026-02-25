from random import randint
from time import sleep
jogadas = 0
acertou = False
jogador = -1

print('-' * 50)
print('Bem-vindo ao jogo de advinhação V.2.0'.center(50))
print('-' * 50)

computador = randint(0, 10)
print('O computador está pensando em um número entre 0 e 10...')
print('PENSANDO...')
sleep(1)
print('O computador pensou!')

while not acertou:
    jogador = int(input('Digite o seu palpite sobre qual número o computador pensou: ').strip())
    jogadas += 1 
    if jogador > computador:
        print('Menos... tente novamente!')
    elif jogador < computador:
        print('Mais... tente novamente!')
    else:
        print('Parabéns, você acertou!')
        acertou = True
print(f'Você precisou de {jogadas} jogadas para vencer o jogo!')