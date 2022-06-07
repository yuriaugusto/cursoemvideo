# Desafio 027: faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente. 
# exemplo: Enzo Lorenzo Bragança Valadares, primeiro Enzo, ultimo Valadares

nome = str(input('Digite o nome completo: ')).strip()

primeiro = nome.split()
print(primeiro[0])
print(primeiro[len(primeiro) - 1])