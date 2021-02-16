"""
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""

while True:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1 + n2) / 2
    print('A sua nota {} mais a {}, dá uma média de {}' .format(n1, n2, media))
    if media < 5:
        print('Você foi REPROVADO')
    elif 5 <= media < 7:
        print('Você está de RECUPERAÇÃO')
    elif media >= 7:
        print('Você foi APROVADO')

