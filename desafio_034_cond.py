# escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento

# para salarios superiores a 1250 calcule um aumento de 10%. Para ps inferiores ou iguais, o aumento é de 15%

salario = float(input('Informe o salário atual: R$'))

if salario >= 1250:
    print(f'O aumento do seu salário é de 10%, totalizando R${salario + (salario * 10/100):.2f}. \nUm aumento de R${salario * 10/100}.')
else:
    print(f'O aumento do seu salário é de 15%, totalizando R${salario + (salario * 15/100):.2f}. \nUm aumento de R${salario * 15/100}.')