# desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

# Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.

lado1 = int(input('Digite o comprimento da primeira reta do triângulo: '))
lado2 = int(input('Digite o comprimento da segunda reta do triângulo: '))
lado3 = int(input('Digite o comprimento da terceira reta do triângulo: '))

# if ((lado2 - lado3) < lado1 < (lado2 + lado3)) and ((lado1 - lado3) < lado2 < (lado1 + lado2)) and ((lado1 - lado2) < lado3 < (lado1 + lado2)):
if lado1 < lado2 + lado3 and lado2 < lado1 + lado2 and lado3 < lado1 + lado2:
    print('É possível formar um triângulo!')
else:
    print('Com essas medidas é impossível formar um triângulo.')