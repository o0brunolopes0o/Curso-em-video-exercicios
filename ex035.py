"""
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.
"""
print('-=-' * 20)
print('             Analisador de triangulos           ')
print('-=-' * 20)
print('Me informe as medidas ')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('-=-' * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM formar um triângulo')
else:
    print('Os segmentos NÃO podem formar um triângulo')
