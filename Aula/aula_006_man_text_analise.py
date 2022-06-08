# ANÁLISE
frase = 'Curso em vídeo python'
print(frase)
# mostra comprimento dos caracteres
print(len(frase))
# contar caractere escolhido
print(frase.count('o'))
# contar caractere selecionado, dentro de determinado fatiamento, nesse caso, do 0 ao 13
print(frase.count('o', 0, 13))
# encontrar determinados caracteres
print(frase.find('deo'))
# se colocar uma string que não existe, ele retorna o valor -1 (está dando erro)
#print(frase.find('android')