#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Digite quanto dinheiro você tem na carteira? R$'))
dolar = 4.86
conv = carteira / dolar

print('Com R${:.2f} reais você consegue comprar US${:.2f} doláres.'.format(carteira, conv))