# elabora um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
# a vista dinheiro/cheque: 10% de desconto
# a vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input("Qual o valor a ser pago? R$"))

metodo = int(input("""Escolha o método de pagameto abaixo: 
    1 - a vista (dinheiro ou cheque)
    2 - a vista (cartão)
    3 - 2 parcelas no cartão
    4 - 3 parcelas ou mais no cartão
"""))

if metodo == 1:
    print(f'Para pagamentos a vista em dinheiro ou cheque, desconto de 10%. O valor final do produto é R${preco-preco*(10/100):.2f}.')
elif metodo == 2:
    print(f'Para pagamentos no débito, desconto de 5%. Valor final do produto: R${preco-preco*(5/100):.2f}.')
elif metodo == 3:
    print(f'O valor do produto é R${preco:.2f}. Em duas vezes no cartão a parcela fica R${preco/2:.2f}.')
elif metodo == 4:
    qtparc = int(input('Quantas parcelas você quer dividir? '))
    print(f'Para dividir em {qtparc} parcelas, temos um acréscimo de 20%. Valor final do produto é R${preco+preco*(20/100):.2f} e o valor por parcela será {(preco+preco*(20/100))/qtparc:.2f}.')
else:
    print('Selecione o valor correto.')