'''
# tarefa 001
print('Olá, mundo!')

# tarefa 002 - mesma coisa
msg = 'Olá, mundo!'
print(msg)
'''

# tarefa 003 - usando print de diferentes maneiras
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, ', nome, '.')
print(f'É um prazer te conhecer, {nome}.')
print('É um prazer te conhecer, {}.'.format(nome))


# usando alinhamento no print
nome = input('Qual seu nome? ')
# print com 10 caracteres (mesmo que o nome seja menor)
print(f'Prazer em te conhecer {nome:10}!')
# print com alinhamento à direita
print(f'Prazer em te conhecer {nome:>10}!')
# print com alinhamento à esquerda
print(f'Prazer em te conhecer {nome:<10}!')
# print com alinhamento centralizado
print(f'Prazer em te conhecer {nome:^10}!')
# print com alinhamento centralizado e caracteres ao redor
print(f'Prazer em te conhecer {nome:=^10}!')