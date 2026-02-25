from random import randint
from time import sleep

print('-' * 50)
print('Bem-vindo ao jogo de Jokenpo (pedra, papel tesoura)')
print('-' * 50)

opcoes = ['pedra', 'papel', 'tesoura']
jogadas = randint(0, 2)
computador = opcoes[jogadas]
print('''Suas opções: 
      [0] pedra
      [1] papel
      [2] tesoura''')
jogador = int(input('Digite sua jogada de Jokenpo: ').strip())

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

if computador == opcoes[jogador]:
    print(f'O jogador escolheu {opcoes[jogador]} e o computador escolheu {computador}!')
    print('Temos um EMPATE!!!')
elif computador == 'pedra' and opcoes[jogador] == 'tesoura':
    print(f'O jogador escolheu {opcoes[jogador]} e o computador escolheu {computador}!')
    print('Vitória do computador!!!')
elif computador == 'tesoura' and opcoes[jogador] == 'papel':
    print(f'O jogador escolheu {opcoes[jogador]} e o computador escolheu {computador}!')
    print('Vitória do computador!!!')
elif computador == 'papel' and opcoes[jogador] == 'pedra':
    print(f'O jogador escolheu {opcoes[jogador]} e o computador escolheu {computador}!')
    print('Vitória do computador!!!')
elif opcoes[jogador] == 'pedra' and computador == 'tesoura':
    print(f'O computador escolheu {computador} e o jogador escolheu {opcoes[jogador]}!')
    print('Vitória do jogador!!!')
elif opcoes[jogador] == 'tesoura' and computador == 'papel':
    print(f'O computador escolheu {computador} e o jogador escolheu {opcoes[jogador]}!')
    print('Vitória do jogador!!!')
elif opcoes[jogador] == 'papel' and computador == 'pedra':
    print(f'O computador escolheu {computador} e o jogador escolheu {opcoes[jogador]}!')
    print('Vitória do jogador!!!')
else:
    print('Jogada inválida!')