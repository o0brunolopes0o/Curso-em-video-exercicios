preco = float(input('Qual é o preço do produto?: R$ '))
novo = preco-((preco * 5 / 100))

print('O produto que custava R${:.2f} com desconto de 5% passou a custar R${:.2f}'.format(preco, novo))


