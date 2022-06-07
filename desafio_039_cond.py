#faça um programa que leia o ano de nascimento de um jovem e informa de acordo com a sua idade:
# se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento
#seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

nascimento = int(input('Em que ano nasceu jovem gafanhoto? '))
atual = date.today().year
idade = atual - nascimento

if idade == 18:
    print('Chegou a sua hora de pintar sarjeta meu companheiro.')
elif idade < 18:
    print(f'Ainda ta com cheiro de talco nenezão. Só vai pintar sarjeta daqui {18-idade} anos. Ou seja, só em {atual +(18-idade)}')
else:
    print(f'Já deve estar até com hérnia de disco né meu senhor. Já prestou seu serviço ao país há {idade-18} anos, muita sarjeta pintada. Foi babar ovo de militar em {atual - (idade-18)}')