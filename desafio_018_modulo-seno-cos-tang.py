# faça um programa que leia um ãngulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = float(input('Digite o ângulo: '))

print(f'Para o ângulo {angulo}º:\nO cosseno é {math.cos(math.radians(angulo)):.2f}.\nO seno é {math.sin(math.radians(angulo)):.2f}.\nE a tangente é {math.tan(math.radians(angulo)):.2f}.')

