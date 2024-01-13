#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

numero = int(input('Digite um número para descobrir seu dobro, triplo e raiz quadrada: '))

dobro = numero *2
triplo = numero *3
raiz_quadrada = math.sqrt(numero) 

print('O dobro do número {} é {}, o triplo é {} e a raiz quadrada é {}.'.format(numero, dobro, triplo, raiz_quadrada))