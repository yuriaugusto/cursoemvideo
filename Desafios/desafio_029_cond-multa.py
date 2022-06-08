# escreva um programa que leia a velocidade de um carro. 

# se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7 mangos por cada km acima do limite

velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print(f'Parabéns Barnabé, você tomou uma multa por estar acima da velocidade! O valor da sua multa é R${(velocidade - 80) * 7:.2f}.\nVocê estava a {velocidade}km/h, ultrapassando por {velocidade - 80}km/h o limite da via.')
else:
    print('Tudo na santa paz irmão! Sem multa hoje.')