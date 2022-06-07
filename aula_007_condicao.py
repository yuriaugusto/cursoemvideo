# o famigerado if elif else

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo hein, ta rasgando.')
else:
    print('Curte um museu hein meu chapa?')

# modo simplificado de condicional
print('Carro novo' if tempo <= 3 else 'Carro velho')