# refazer o desafio 035, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# equilátero: todos os lados iguais; isósceles: dois lados iguais; escaleno: todos os lados diferentes

lado1 = int(input('Digite o comprimento da primeira reta do triângulo: '))
lado2 = int(input('Digite o comprimento da segunda reta do triângulo: '))
lado3 = int(input('Digite o comprimento da terceira reta do triângulo: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado2 and lado3 < lado1 + lado2:
    print('É possível formar um triângulo!')
# podemos fazer a comparação diretamente um com o outro
    if lado1 == lado2 == lado3:
        print('Esse é um triângulo equilátero, todos os lados tem a mesma medida.')
# ao invés de montar a formula para o isosceles, que é mais complicado. Monte com o mais fácil e deixe o mais complicado para o else
#    elif lado1 == lado2 and lado1 != lado3 or lado2 == lado3 and lado1 != lado2:
#        print('Esse é um triãngulo isósceles, há pelo menos 2 lados iguais.')
    elif lado1 != lado2 != lado3 != lado1:
        print('Triângulo escaleno, onde não há lados iguais.')
    else:
        print('Triângulo isosceles, onde há apenas dois lados iguais.')
else:
    print('Com essas medidas é impossível formar um triângulo.')