"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar()
. A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.
"""
from time import sleep
from random import randint


def sorteio(num):
    for c in range(0, 5):
        num.append(randint(1, 6))
    print(f'Sorteamos 5 valores da lista: \n', end=' ')
    for g in num:
        print(g, end=' ', flush='True')
        sleep(0.4)
    print(' PRONTO')


def somaPar(som):
    soma = 0
    for p in som:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores pares de {som}, temos {soma}')
    print('-=' * 30)


# PROGRAMA PRINCIPAL


numeros = list()
sorteio(numeros)
somaPar(numeros)
