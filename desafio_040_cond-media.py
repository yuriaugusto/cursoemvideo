# crie um programa que leia duas ntoas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# abaixo de 5.0 está reprovado, entre 5 e 6,9 recuperação e se média igual ou maior que 7.0 está aprovado

nota1 = float(input('Qual a nota da primeiro prova do jumento celestino? '))
nota2 = float(input('Qual a nota da segunda prova do oreia seca? '))
media = (nota1 + nota2)/2

if media < 5:
    print(f'Eu disse que era burro, não da pra passar com {media}.')
elif 5 <= media < 6.9:
    print(f'Vai ter que fazer recuperação, pois {media} não é suficiente não.')
else:
    print(f'PASSOU MISERAVI! NOTÃO HEIN: {media}')