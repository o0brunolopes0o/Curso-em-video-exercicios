"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para
vencer.
"""

import random
from time import sleep
palpite = 1
computador = random.randint(1, 3)  # computador pensa
print('-=-' * 20)
print('Vou pensar em um número entre 1 e 10. Tente adivinhar...')
print('-=-' * 20)
while True:
    jogador = int(input('Entre 1 e 10 qual número eu pensei?: '))
    print('Processando...')
    sleep(1)
    if computador == jogador:
        print('Parabéns você acertou!!!')
        print('Acertou com {} palpites.' .format(palpite))
        break
    elif computador != jogador:
        palpite +=1
        if jogador < computador:
            print('Abaixo do valor... Tente novanente...')
        elif jogador > computador:
            print('Acima do valor... Tente novamente...')

        print('Tente novamente...')
