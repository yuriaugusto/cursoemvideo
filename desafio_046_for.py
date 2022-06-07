# faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0 com uma pausa de um segundo entre eles
from time import sleep

for c in range(11, 0, -1):
    print(c-1)
    sleep(1)