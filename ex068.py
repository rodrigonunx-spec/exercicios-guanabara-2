from random import randint

print('-' * 50)
print('Bem-vindo ao jogo de Par ou Ímpar em Python!'.center(50))
print('-' * 50)
vitorias = 0

while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor de 0 a 10: ').strip())
    jogada = ' '
    while jogada not in 'PI':
        jogada = str(input('Par ou Ímpar? [P/I]: ').strip().upper()[0])
    jogo = jogador + computador
    if jogo % 2 == 0 and jogada == 'P':
        print(f'Você jogou {jogador} e o computador jogou {computador}. Resultado {jogo} deu PAR!')
        print('=-=' * 15)
        print('Você GANHOU! PARABÉNS!!')
        print('=-=' * 15)
        print('Vamos continuar o jogo')
        vitorias += 1
    elif jogo % 2 == 0 and jogada == 'I':
        print(f'Você jogou {jogador} e o computador jogou {computador}. Resultado {jogo} deu PAR!')
        print('-=' * 10)
        print('Você PERDEU!!')
        print('-=' * 10)
        print(f'GAME OVER!!! Você venceu {vitorias} vezes consecutivas!')
        break
    elif jogo % 2 == 1 and jogada == 'I':
        print(f'Você jogou {jogador} e o computador jogou {computador}. Resultado {jogo} deu ÍMPAR!')
        print('=-=' * 15)
        print('Você GANHOU! PARABÉNS!!')
        print('=-=' * 15)
        print('Vamos continuar o jogo')
        vitorias += 1
    else:
        print(f'Você jogou {jogador} e o computador jogou {computador}. Resultado {jogo} deu ÍMPAR!')
        print('-=' * 10)
        print('Você PERDEU!!')
        print('-=' * 10)
        print(f'GAME OVER!!! Você venceu {vitorias} vezes consecutivas!')
        break

print('\nEsperamos que tenha gostado do nosso jogo de PAR ou ÍMPAR em Python!')
print('Por favor, dê um feedback sobre o jogo para que possamos melhorá-lo!')
print('Tenha um bom dia e volte sempre!!')