print('=' * 40)
print('Boas vindas ao SuperMercado Xavier!'.center(40))
print('=' * 40)

valor = 0
mais_1000 = 0
mais_barato = ''
preco_barato = 0
contador = 0

while True:
    produto = str(input('Qual o produto que deseja levar: ').strip())
    preco = float(input('Informe o preço do produto que deseja levar: ').strip())
    contador += 1
    valor += preco
    if preco > 1000:
        mais_1000 += 1
    if contador == 1:
        preco_barato = preco
        mais_barato = produto
    else:
        if preco < preco_barato:
            preco_barato = preco
            mais_barato = produto

    continuar = str(input('Mais algum produto que deseja levar? [S/N]: ').strip().upper()[0])
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Mais algum produto que deseja levar? [S/N]: ').strip().upper()[0])
    if continuar == 'N':
        break
print('\nObrigada por comprar no SuperMercado Xavier! Aqui está um relatório das suas compras: ')
print(f'Você comprou um total de {contador} produtos!')
print(f'O valor total da sua compra ficou em R${valor:.2f}')
print(f'Você comprou {mais_1000} produtos cujo preço era mais de R$1000.00')
print(f'O produto mais barato que você comprou foi um(a) {mais_barato} no valor de R${preco_barato:.2f}')
print('\nAgradecemos a sua preferência pelos nossos serviços. Obrigado e volte sempre!!')