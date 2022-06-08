# crie um prograa que faça o computador jogar jokenpô com você
from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('&&&'*10)
print('''Opções:
0 - Pedra
1 - Papel
2 - Tesoura
''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOO')
print('-%'*15)
print(f'O jogador jogou: {itens[jogador]}')
print(f'O computador jogou: {itens[computador]}')
print('-%'*15)

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    else:
        print('COMPUTADOR VENCEU!')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU A PARTIDA!')
    elif jogador == 1:
        print('EMPATE, TENTE DE NOVO!')
    else:
        print('JOGADOR LEVOU ESSA!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU A PARTIDA!')
    elif jogador == 1:
        print('JOGADOR SE FUDEU!')
    else:
        print('EMPATE MOÇO!')
else:
    print('Opção inválida jumento!')
