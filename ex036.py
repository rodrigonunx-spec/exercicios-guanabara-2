print('-' * 100)
print('Bem-vindo ao empréstimo de banco!')
print('Digite os valores abaixo para que possamos verificar se está apto à fazer o empréstimo!')
print('-' * 100)
casa = float(input('Digite o valor da casa que deseja comprar: ').strip())
sal = float(input('Digite o valor do seu salário mensal: ').strip())
anos = int(input('Digite em quantos anos planeja pagar a casa: ').strip())
limite = (sal * 30/100)
prestacao = (casa / anos) / 12

if prestacao > limite:
    print(f'O seu empréstimo foi negado, pois a prestação no valor de R${prestacao:.2f} excede o seu limite que é de R${limite:.2f} por mês!')
elif prestacao == limite:
    print(f'O seu empréstimo foi aceito, mas preste atenção à prestação mensal no valor de R${prestacao:.2f} por mês durante {anos} anos!')
else:
    print(f'O seu empréstimo foi aceito, você pagará R${prestacao:.2f} por mês durante {anos} anos!')