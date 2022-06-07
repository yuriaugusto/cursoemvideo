# Desafio 025: cria um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome (true or false)

nome = str(input('Digite o nome completo de um caboclo: ')).strip()

var = 'SILVA' in nome.upper()
print(var)