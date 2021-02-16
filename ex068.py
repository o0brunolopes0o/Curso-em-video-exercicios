"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
V = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    print('Você jogou {} e o computador jogou {}. Total de {}'. format(jogador, computador, total))
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
            V += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
            print('Você VENCEU!!')
            V += 1
    else:
        print('Você PERDEU!!')
        break
    print('Vamos jogar novemante... ')
print('GAME OVER! Você venceu {} vezes.' .format(V))
