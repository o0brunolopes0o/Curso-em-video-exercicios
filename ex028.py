import random
from time import sleep


computador = random.randint(0, 5) #COMPUTADOR PENSANDO

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Qual número eu pensei?: '))
print('Processando...')
sleep(3)

if jogador == computador:
    print('Parabéns você conseguiu acertar...')
else:
    print('Ganhei! Eu pensei em {} e não no {}' .format(computador, jogador))




