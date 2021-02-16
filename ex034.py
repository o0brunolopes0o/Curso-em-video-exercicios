"""
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Digite o valor do salário R$: '))

if salario > 1250:
    nsalario = salario * (10 / 100)
    print('Seu salário com 10% a mais fica em {:.2f} totalizando seu salario em {:.2f}'
          .format(nsalario, (nsalario+salario)))

if salario <= 1250:
    nsalario = salario * (15 / 100)
    print('Seu salário com 15% a mais fica em {:.2f} totalizando seu salario em {:.2f}'
          .format(nsalario, (nsalario + salario)))
