# desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre o seu status de acordo com a tabela:
# abaixo de 18.5 = abaixo do peso
# entre 18.5 e 25 = peso ideal
# 25 até 30 = sobrepeso
# 30 até 40 = obesidade
# acima de 40 = obesidade mórbida

peso = float(input('Quanto você está pesando (em kg) Gracyane Barbosa? '))
altura = float(input('Qual a sua altura (em metros)? '))
imc = peso/altura**2
print(f'Seu IMC é: {imc:.1f}.')

if imc < 18.5:
    print('Abaixo do peso. Precisa de uma sustânça jovem.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso. Acho bom começar uma dieta.')
elif 30 <= imc < 40:
    print('Obesidade! Chega de pizza fofolete!')
else:
    print('Sério amigo. Você precisa fazer fotossíntese por umas semanas.')