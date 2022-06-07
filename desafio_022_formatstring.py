# Desafio 022: crie um programa que leia o nome completo de uma pessoa e mostre: 1 o nome com todas as letras maiúsculas, 2 o nome com todas minúsculas, 3 quantas letras ao todo (sem considerar espaços), 4 quantas letras tem o primeiro nome

nome = str(input('Digite o nome do camarada: ')).strip()
#nome = 'Jose Aldo'

print(nome.upper())
print(nome.lower())

# 3 e 4
dividido = nome.split()
print(len(''.join(dividido)))

print(len(dividido[0]))

# outra maneira de fazer o 3 e 4
print(len(nome) - nome.count(' '))

print(nome.find(' '))