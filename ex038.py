while True:
    n2 = int(input('Digite o segundo número: '))
    n1 = int(input('Digite o primeiro número: '))

    if n1 > n2:
        print('O primeiro número é maior que o segundo \n')
    elif n2 > n1:
        print('O segundo número é maior que o primeiro \n')
    else:
        print('Os números são iguais \n')
