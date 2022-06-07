#faça um programa que leia o peso de cinco pessoas. No final, mostre quem foi o maior e o menor peso lidos.

maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input("Qual o peso em kg? "))
    if maior == 0 or menor == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    
print(maior, menor)