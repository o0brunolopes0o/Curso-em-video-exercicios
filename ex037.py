"""
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
while True:
    escolha = int(input('Escolha para qual fator converter \n (1) Binario \n (2) Octal \n (3) Hexadecimal \n (4) SAIR'
                        '\n R: '))
    if escolha == 4:
        break

    numero = int(input('Digite um numero inteiro: '))

    if escolha == 1:
        print('Você escolheu converter para Binário.')
        print('O valor {} convertendo em binario fica em {} \n'.format(numero, bin(numero)[2:]))

    elif escolha == 2:
        print('Você escolheu converter para Binário.')
        print('O valor {} convertendo em octal fica em {} \n'.format(numero, oct(numero)[2:]))

    elif escolha == 3:
        print('Você escolheu converter para Binário.')
        print('O valor {} convertendo em hexadecimal fica em {} \n'.format(numero, hex(numero)[2:]))

    else:
        print('Tente novamente.')