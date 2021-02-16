"""
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""

""""
while True:
    opcao = int(input('Digite:\n (1) Para calcular o IMC \n (2) Para SAIR \n R: '))
    if opcao == 1:
        altura = float(input('Digite a altura em m e cm: '))
        peso = float(input('Digite o peso atual: '))
        imc = peso / (altura * altura)
        print('Seu IMC atual é de {:.1f}'.format(imc))
        if imc < 18.5:
            print('Abaixo do peso')
        elif 18.5 < imc < 25:
            print('Peso ideal')
        elif 25 < imc < 30:
            print('Sobrepeso')
        elif 30 < imc < 40:
            print('Obesidade')
        elif imc > 40:
            print('Obesidade Morbida')

    if opcao == 2:
        break
"""
while True:
    opcao = int(input('Digite:\n (1) Para calcular o IMC \n (2) Para SAIR \n R: '))
    if opcao == 1:
        altura = float(input('Digite a altura em m e cm: '))
        peso = float(input('Digite o peso atual: '))
        imc = peso / (altura * altura)
        print('Seu IMC atual é de {:.1f}'.format(imc))
        icms = [
        [0, 18.5, 'Abaixo do peso'],
        [18, 25, 'Peso ideal'],
        [25, 30, 'Sobrepeso'],
        [30, 40, 'Obesidade'],
        [40, 100, 'Obesidade Morbida']
        ]
        for i in icms:
            if i[0] < imc <= i[1]:
                print(i[2])
    elif opcao == 2:
        break