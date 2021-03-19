"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
a) Quantidade de notas
b) A menor nota
c) A média da turma
d) A situação(opcional)
"""


def notas(*n, sit=False):
    """
    n -> uma ou mais notas dos alunos (aceita várias)
    sit -> valor opicional, indicando se deve ou não adicionar a situação
    return -> dicionário com várias informações sobre a situação de cada turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'APROVADO'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'REPROVADO'
    return r


# Programa Principal

"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
resp = notas(n1, n2, n3, n4, sit=True)

print(resp)
"""

while True:
    decisao = str(input('Quer digitar uma nota? [S/N]: '))
    if decisao in 'Nn':
        print('Fim!')
        break
    elif decisao in 'Ss':
        n1 = float(input('Digite uma nota: '))
        notas += n1

resp = notas(n1, sit=True)
print(resp)
