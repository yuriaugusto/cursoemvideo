# a confederação nacioal de natação precisa de um programa que leia o ano de nascimento de um atleta e mostra sua categoria, de acordo com a idade:
# até 9 anos é mirim, até 14 anos infantil; até 19 anos junior, até 20 senior, acima de 20 master
 
from datetime import date

atual = date.today().year
nascimento = int(input('Qual o ano de nascimento do atleta? '))
idade = atual - nascimento

if idade <= 9:
    print('Atleta mirinzão!')
elif 9 < idade <= 14:
    print('Atleta infantil.')
elif 14 < idade <= 19:
    print('Atleta junior.')
elif 19 < idade <= 20:
    print('Atleta senior, um monstro.')
else:
    print('Já é o pica das galáxias, atleta master.')