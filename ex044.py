"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros (no valor total do produto)
"""
produto = float(input('Digite o valor do produto R$: '))
avistad = produto - (produto * (10/100))
avistac = produto - (produto * (5/100))
parcela = produto / 2
parcelaj = (produto * (20/100)) + produto
parcelajp = parcelaj / 3

print('A vista com 10% de desconto R$: {}' .format(avistad))
print('A vista com 5% de desconto R$: {}' .format(avistac))
print('Parcelado sem juros fica em 2x de R$: {}' .format(parcela))
print('Parcelado com 20% de juros fica em 3x de R$: {} \n Juros ficou em R$: {}' .format(parcelajp, parcelaj))