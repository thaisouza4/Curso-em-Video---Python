#Escreva um progrmaa que leia um valor em metros e o exiba covertido em centímetros e milímetros.

metros = int(input('Quantos metros você quer converter em centímetros e milímetros? '))

cent = metros / 10**-2
mil = metros / 10**-3

print(f'A conversão de {metros} metros em centímetros é {cent} e em milímetro é {mil}.')