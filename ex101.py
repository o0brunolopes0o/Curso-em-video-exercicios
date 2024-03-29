"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(ano):
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPICIONAL.'
    elif idade >= 18 < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


while True:
    nasc = int(input('Digite o ano de nascimento (999 para sair): '))
    if nasc == 999:
        print('FIM!')
        break
    else:
        print(voto(nasc))
