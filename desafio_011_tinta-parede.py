print('Desafio 011:\nFaça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m².')

altura = float(input('Qual a altura da parede: '))
largura = float(input('Qual a largura da parede: '))
area = altura * largura

print(f'Para pintar uma parede com {altura}m de altura e {largura}m de largura, totalizando uma área de {area:.2f}m², será necessário {(area/2):.2f} litros de tinta.')