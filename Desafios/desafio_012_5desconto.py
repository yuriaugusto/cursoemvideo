print('Desafio 012:\nFaça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')

preco = float(input('Digite o preço do produto: '))

print(f'O preço do produto com 5% de desconto é: R${preco - (preco * (5/100))}.')