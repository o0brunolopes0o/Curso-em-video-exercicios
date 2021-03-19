"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e
o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""


def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)


# Programa Principal

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO')
