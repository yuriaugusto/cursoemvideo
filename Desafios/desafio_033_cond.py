# faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

'''
if num3 <= num1 >= num2:
    if num2 > num3:
        print(f'O maior número é {num1} e o menor é {num3}.')
    else:
        print(f'O maior número é {num1} e o menor é {num2}.')
elif num1 <= num2 >= num3:
    if num1 > num3:
        print(f'O maior número é {num2} e o menor é {num3}.')
    else:
        print(f'O maior número é {num2} e o menor é {num1}.')
elif num1 <= num3 >= num2:
    if num1 > num2:
        print(f'O maior número é {num3} e o menor é {num2}.')
    else:
        print(f'O maior número é {num3} e o menor é {num1}.')
'''

# outro método para calcular o menor, usando as variáveis
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
# agora vamos calcular o menor
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O maior valor foi {maior} e o menor foi {menor}.')