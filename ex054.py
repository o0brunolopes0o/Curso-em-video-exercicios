"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: ' .format(pess)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos.' .format(idade))
    if idade >= 21:
        totmaior += 1
        print('Essa pessoa é maior')
    else:
        totmenor += 1
        print('Essa pessoa é menor')
print('Ao todo tivemos {} pessoas maiores de idade' .format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade' .format(totmenor))
