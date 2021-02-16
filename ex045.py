"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep

while True:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    [ 3 ] SAIR''')
    jogador = int(input('Qual sua jogada? R: '))
    if jogador == 3:
        break
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(1)
    print('-=-' * 20)
    print('Computador jogou {}' .format(itens[computador]))
    print('Jogador jogou {}' .format(itens[jogador]))
    print('-=-' * 20)



    if computador == 0: #computador jogou PEDRA
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCEU!')
        elif jogador == 2:
            print('COMPUTADOR VENCEU!')
        else:
            print('JOGADA INVÁLIDA')

    elif computador == 1: #computador jogou PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCEU!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCEU!')
        else:
            print('JOGADA INVALIDA!')
    elif computador == 2: #computador jogou TESOURA
        if jogador == 0:
            print('JOGADOR VENCEU!')
        elif jogador == 1:
            print('COMPUTADOR VENCEU!')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('JOGADA INVALIDA')