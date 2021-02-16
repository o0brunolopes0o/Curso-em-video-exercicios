"""
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
somaidade = 0
for p in range(1, 5):
    print('----- {}ª Pessoa -----' .format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos' .format(mediaidade))
