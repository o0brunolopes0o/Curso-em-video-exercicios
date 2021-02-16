"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""
times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético', 'Internacional',
         'Atlético-PR', 'Botafogo', 'Goias', 'Corinthians', 'Grêmio',
         'Bahia', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Vasco da Gama',
         'Cruzeiro', 'Fluminense', 'Chapecoence', 'CSA', 'Avaí')
while True:
    op = int(input('''
    [ 0 ] Sair do programa
    [ 1 ] Imprimir os 5 primeiros colocados
    [ 2 ] Imprimir os 5 últimos colocados
    [ 3 ] Imprimir Classidicação dos times
    [ 4 ] Imprimir os times em ordem alfabética.
    [ 5 ] Posição do time da Chapecoense
    Sua opção: '''))

    if op == 0:
        print('Fim do programa')
        break
    elif op == 1:
        for time in range(0, 5):
            print('-=-' * 30)
            print(f'{time + 1}º {times[time]}')
    elif op == 2:
        for time in range(16, 20):
            print(f'{time + 1}º {times[time]}')
    elif op == 3:
        for time in range(0, 20):
            print(f'Times em ordem alfabéticas: {sorted(times)}')
    elif op == 4:
        print(f'Times por ordem alfabética: {sorted(times)}')
    elif op == 5:
        esctime = str(input('Escolha o time da busca: '))
        print(f'Chapecoence está na {times.index(esctime)+1} posição.')
    else:
        print('Oção inválida tente novamente...')
