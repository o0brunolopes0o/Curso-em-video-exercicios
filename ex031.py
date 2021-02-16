dist = float(input('Digite a distancia em KM: '))

if dist <= 200:
    valor = dist * 0.50
    print('O valor da corrida será de {}' .format(valor))
elif dist > 200:
    valor = dist * 0.45
    print('O valor da corrida será de {}' .format(valor))