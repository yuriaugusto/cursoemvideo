#crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date
maior = 0
menor = 0

for c in range(0, 7):
    nascimento = int(input("Digite o nascimento: "))
    if (date.today().year - nascimento > 18):
        maior += 1
    else:
        menor += 1
print(f"Temos {maior} pessoas maiores de idade, e {menor} pessoas menores de 18 anos.")