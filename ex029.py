velocidade = float(input('Velocidade atual do carro: '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade de 80Km/h' )
    multa = (velocidade - 80) * 7
    print('O valor da multa é de R$ {:.2f}!' .format(multa))
else:
    print('Tenha um bom dia siga com segurança')

