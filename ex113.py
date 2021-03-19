"""
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(f):
    while True:
        try:
            valor = int(input(f))
        except (ValueError, TypeError):
            print('ERRO: Digite um valor inteiro!')
            # joga de novo para o while
            continue
        except KeyboardInterrupt:
            return 0
        else:
            # Return quebrando laço
            return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Digite um valore real!')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return valor


n = leiaFloat('Digite um valor real: ')
print(n)
n = leiaInt('Digite um valor inteiro: ')
print(n)
