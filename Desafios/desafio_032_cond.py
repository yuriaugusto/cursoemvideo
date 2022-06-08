# faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

#importando modulo date
from datetime import date

ano = int(input('Digite um ano!\nColoque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 10 == 0 and ano % 100 == 0 and ano % 400 ==0:
    print(f'O ano {ano} é bissexto!')
elif ano % 4 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')