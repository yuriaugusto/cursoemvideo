# desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando 0,5 cents por km para viagens de até 200km e 0,45 cents para viagens mais longas

dist = int(input('Qual a distância da viagem que deseja realizar em km? '))


# deixando o código mais curto
'''
if dist <= 200:
    print(f'O valor da passagem é R${dist * 0.5:.2f}')
    
else:
    print(f'O valor da passagem é R${dist * 0.45:.2f}')
'''
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print(f'O valor da passagem é R${preco}')