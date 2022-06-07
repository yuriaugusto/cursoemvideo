# TRANSFORMAÇÃO

frase = 'Curso em vídeo Python'
print(frase + ': essa é a frase crua')

# substituir string na frase
print(frase.replace('Python', 'android'))
# usando upper para deixar em maiúsculo
print(frase.upper())
# ao contrario do upper, deixa tudo em minúsculo
print(frase.lower())
# capitalize deixa apenas o primeiro caractere maiúsculo
print(frase.capitalize())
# já o title deixa todos os primeiros caracteres de cada palavra em maiúsculo
print(frase.title())

frase2 = '   Aprenda python  '

# para remover o espaço antes e depois da string, aqueles inuteis
print(frase2.strip())
# também podemos usar o strip para remover os espaços apenas da direita quanto da esquerda: rstrip e lstrip
print(frase2.rstrip())
print(frase2.lstrip())

