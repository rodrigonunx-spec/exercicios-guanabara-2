print('-' * 60)
print('Bem-vindo à central de pagamentos em Python!')
print('-' * 60)

print('Veja as precificações: ')
print('(1) À vista cheque/dinheiro: 10% de desconto!')
print('(2) À vista no cartão: 5% de desconto!')
print('(3) Parcelado em 2x no cartão: Preço normal!')
print('(4) Parcelado em 3x ou mais no cartão: 20% de juros!')

preco = float(input('Digite o preço do produto que deseja comprar: ').strip())
escolha = int(input('Digite qual das formas de pagamento acima gostaria de usar: ').strip())

if escolha == 1:
    print(f'O valor original do produto é R${preco:.2f}, mas pagando à vista no dinheiro/cheque fica R${preco - (preco * 10 / 100):.2f}!')
elif escolha == 2:
    print(f'O valor origninal do produto é R${preco:.2f}, mas pagando à vista no cartão fica R${preco - (preco * 5 / 100):.2f}!')
elif escolha == 3:
    print(f'O valor oringinal do produto é R${preco:.2f}, mas parcelando em 2x vezes no cartão o preço não tem alteração')
    print(f'Valor de cada parcela: R${preco / 2:.2f}')
elif escolha == 4:
    parcela = int(input('Digite a quantidade de parcelas: ').strip())
    juros = preco + (preco * 20 / 100)
    if parcela < 3:
        print('Número de parcelas inválido para essa forma de pagamento. Tente novamente.')
    else:
        print(f'O valor original do produto é R${preco:.2f}, mas parcelando em 3x ou mais tem 20% de juros. Portanto o valor passa a ser R${juros:.2f}!')
        print(f'Valor de cada umas das {parcela} parcelas: R${juros / parcela:.2f}')