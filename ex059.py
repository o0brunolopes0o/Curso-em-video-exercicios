"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
while True:
    escolha = int(input('\nEscola uma opção:'
                        '\n[1] Soma'
                        '\n[2] Multiplica'
                        '\n[3] Maior'
                        '\n[4] Novos números'
                        '\n[5] Sair'
                        '\nR: '))
    if escolha == 1:
        print('\nVocê escolheu SOMAR...')
        sleep(1)
        print('A soma do valor {:.2f} + {:.2f} é igual a {:.2f}'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('\nVocê escolheu MULTIPLICAR...')
        sleep(1)
        print('A a multiplicação do valor {:.2f} * {:.2f} é igual a {:.2f}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        print('\nO maior número foi {:.2f}' .format(max(n1, n2)))
    elif escolha == 4:
        n1 = float(input('\nDigite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif escolha == 5:
        print('\nSaindo do programa...')
        sleep(1)
        break
