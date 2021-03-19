"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


def maior(* num):
    print('-=' * 30)
    print('Analizando os valores...')
    sleep(0.5)
    for c in num:
        print(c, end=' ', flush=True)
        sleep(0.5)
    print(f'\nForam informados {len(num)} valores.')
    sleep(0.5)
    print(f'O maior valor informado foi {max(num)}')

# programa principal


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
