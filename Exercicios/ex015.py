dias = int(input('Digite a quantidade de dias de aluguel: '))
kms = float(input('Digite a quantidade de KMs rodados: '))
pago = (dias * 60) + (kms * 0.15)
print('O valor a ser pago é de R$ {:.2f}'.format(pago))
