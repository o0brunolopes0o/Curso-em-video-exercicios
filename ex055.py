"""
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
peso lidos.
"""
maior = 0
menor = 0
for peso in range(0, 5):
    peso = float(input(f'qual pesso da {peso} pessoa: '))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é {} e o menor pesso {}'.format(maior, menor))

