# escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor é maior
# o segundo valor é maior
# não existem valores maiores, os dois são iguais

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print('O primeiro valor inserido é maior.')
elif num2 > num1:
    print('O segundo valor inserido é maior.')
else:
    print('Não há valores maiores.')