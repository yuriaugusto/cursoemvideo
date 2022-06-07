# manipulação de cadeia de textos

frase = 'Curso em vídeo python'
print(frase)

# FATIAMENTO: se eu colocar a letra 9 entre chaves, vai ser impresso na tela apenas o nono caractere da variável
print(frase[9])
# mostra o intervalo selecionado
print(frase[9:21])
# pulando de dois em dois caracteres
print(frase[9:21:2])
# se omitir o início, ele começa do 0
print(frase[:5])
# do 15 em diante
print(frase[15:])
# quando usamos :: nesse caso pula 3 caracteres, do 9 até o final
print(frase[9::3])


