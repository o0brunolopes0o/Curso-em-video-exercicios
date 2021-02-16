"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
então o empréstimo será negado.
"""

valorcasa = float(input('Qual o valor da casa para empréstimo?: '))
salario = float(input('Qual o seu salário atual?: '))
anos = int(input('Em quantos anos irá quitar?: '))

meses = int(anos * 12)
parcela = float(valorcasa / meses)
calcsalario = float(30/100) * salario
print('O valor máximo das parcelas podem ser de 30% do seu salario ou seja de R${:.2f}'.format(calcsalario))

print('O valor da parcela será de {:.2f} divididos em {} meses' .format(parcela, meses))

if parcela <= calcsalario:
    print('APROVADO')
else:
    print('REPROVADO')


