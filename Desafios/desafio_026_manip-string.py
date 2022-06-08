# Desafio 026: faça um programa que leia uma frase pelo teclado e mostre: 1 quantas vezes aparece a letra 'a', 2 em que posição ela aparece a primeira vez, 3 em que posição ela aparece a última vez

frase = str(input('Digite qualquer porra de frase: ')).strip().upper()

qtd = frase.count('A')
primeira = frase.find('A') + 1
ultima = frase.rfind('A') + 1
print(f'A letra "a" aparece {qtd} vezes na frase.\nA primeira ocorrência da letra "a" é na posição {primeira} e a última na posição {ultima}.')