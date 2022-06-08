# adicionando cores no python
# informar estilo, texto e fundo
# códigos para estilo 0 = none, 1 = bold, 4 = underline, 7 = negative
# código para texto 30 = branco, 31 = vermelho, 32 = verde, 33 = amarelo, 34 azul, 35 roxo, 36 cyan, 37 cinza
# código para background são os mesmos dos códigos do texto, mas na dezena 4
# \033[0;33;44m

print('Olá mundo!')
print('\033[31mOlá mundo!')
print('\033[4;34mOlá mundo!')

listacores = {'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m'
}

print('{}Essa é a cor {}azul e essa é {}amarela.'.format(listacores['limpa'], listacores['azul'], listacores['amarelo']))