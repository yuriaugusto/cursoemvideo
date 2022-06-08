# Desafio 024: crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()
print(cidade)
print(cidade[:5] == 'SANTO')