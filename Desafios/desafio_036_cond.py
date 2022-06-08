# escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o vlor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('\nOlá, bem vindo ao programa de aquisição imobiliária ou teste de pobreza. Só não é mais humilhante do que o caldeirão do Huck.')
casa = int(input('\nQual o valor da casa que vossa senhoria gostaria de adquirir? R$'))
salario = int(input('\nQuanto o senhor ganha para querer comprar uma casa desse valor? Não vamos meter os pés pelas mãos. R$'))
anos = int(input('\nMuito bem, última pergunta. Em quantos anos o senhor vai querer pagar isso? '))

pmensal = casa/(anos*12)
psalario = salario*(30/100)

if pmensal > psalario:
    print('Com essa mixaria de salário, vai ser impossível pagar a casa pobretão.')
else:
    print(f'Opa meu senhor, financiamento aprovado. O valor da sua parcela será R${pmensal} por {anos} anos.')