#faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input("Número inteiro: "))
qtd = 0

for c in range(1, num+1):
    if num % c == 0:
        qtd += 1
if qtd == 2:
    print("É primo.")
else:
    print("Não é primo primo.")