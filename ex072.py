"""
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',)
while True:
    num = int(input('Digite um valor entre 0 e 20: '))
    if 0 <= num <= 20:
        print('Você digitou o numero {}'.format(cont[num]))
        escolha = str(input('Quer digitar outro número? [S/N] R: ')).strip().upper()
        if escolha == 'S':
            print('Você digitou o numero {}'.format(cont[num]))
        if escolha == 'N':
            print('Fim')
            break
