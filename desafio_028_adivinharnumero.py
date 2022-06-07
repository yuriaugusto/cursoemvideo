# escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

# o programa deverá escrever na tela se o usuário venceu ou perdeu

import random

#gerando um número aleatório entre 0 e 5 para ser adivinhado pelo usuário
num = random.randint(0, 5)
print('-=-' * 40)
print('Fala inteligẽncia rara! Vamos lá, vou pensar em um número entre 0 e 5, tenta adivinhar qual é mané.')
print('-=-' * 40)

# jogador tenta adivinhar o número
resposta = int(input('Adivinhe o número: '))
print('Processando...')
# sleep adiciona um tempo de espera para dar um drama
sleep(3)
if resposta == num:
    print(f'ACERTÔ MIZERAVIH! O número é {num}.')
else:
    print(f'Mais sorte na próxima patrão! O correto seria {num}.')


