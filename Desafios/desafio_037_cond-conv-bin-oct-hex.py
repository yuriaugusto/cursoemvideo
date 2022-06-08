# escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal, 3 para hexadecimal

num = int(input("Digite um número inteiro: "))

escolha = int(input("""
    Selecione uma opção e escolha para qual base deseja converter o número?
        1 - conversão para binário;
        2 - conversão para octal;
        3 - conversão para hexadecimal.
        """))

# python faz a conversão automática, utilizando bin, oct e hex. Os números entre colchetes é utilizado para fatiamento e esconder os dois primeiros caracteres, que indicam se são bin, oct e hex.
if escolha == 1:
    print(f"O número {num} em binário é {bin(num)[2:]}.")
elif escolha == 2:
    print(f"O número {num} em octal é {oct(num)[2:]}.")
elif escolha == 3:
    print(f"O número {num} em haxadecimal é {hex(num)[2:]}.")
else:
    print("Opção inválida! Finalizando...")
