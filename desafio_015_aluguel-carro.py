print('Desafio 015:\nEscreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')

km = float(input('Quantos km foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

preco = (km * 0.15) + (dias * 60)

print(f'O carro foi alugado por {dias} dias e rodou {km}km. O preço a ser pago pelo aluguel do carro é R${preco:.2f}.')