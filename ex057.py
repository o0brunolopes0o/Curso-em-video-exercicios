"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja
errado, peça a digitação novamente até ter um valor correto.
"""

sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
print(sexo)
while sexo != 'M' and sexo != 'F':
    print('Valor digitado invalido...')
    sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
print('Fim')
