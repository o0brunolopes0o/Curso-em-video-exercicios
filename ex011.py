larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt

print('Sua parede tem {} x {} e sua área é de {}m²' .format(larg, alt, area))

tinta = area / 2

print('Para pintar essa parede você precisará de {}lts de tinta' .format(tinta))