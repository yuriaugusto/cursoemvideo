# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math

catoposto = float(input('Digite o valor do cateto oposto: '))
catadjacente = float(input('Digite o valor do cateto adjacente: '))

hip = math.sqrt((catoposto ** 2) + (catadjacente ** 2))

# método mais simples usando o módulo
hip = math.hypot(catoposto, catadjacente)


print(f'O triângulo retângulo com cateto oposto {catoposto} e cateto adjacente {catadjacente} tem hipotenusa com comprimento {hip}.')