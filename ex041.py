"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""

from datetime import date

while True:
    atual = date.today().year
    nasc = int(input('Digite a data de nascimento: '))
    idade = atual - nasc
    print('O aluno tem {} anos' .format(idade))
    if idade <= 9:
        print('O aluno está no MIRIM')
    elif idade <= 14:
        print('O aluno está no INFANTIL')
    elif idade <= 19:
        print('O aluno está no JÚNIOR')
    elif idade <= 25:
        print('O aluno está no SÊNIOR')
    elif idade > 25:
        print('O aluno está no MASTER')