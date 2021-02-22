"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palvras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar'
           'trabalhar', 'mercado', 'programador', 'futuro')
for p in palvras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
