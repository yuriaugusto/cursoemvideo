# faça um programa que calcule a soma entre todos os números ímpares que são multiplos de 3 e que se encontram no intervalo de 1 até 500

soma = 0

for c in range(1, 500, 2):
    if (c % 3 == 0):
        soma += c
print(soma)