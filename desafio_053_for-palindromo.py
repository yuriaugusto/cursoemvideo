# crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input("Digite uma frase meu chegado: ")).replace(" ", "").upper()
inverso = ""

# é possível fazer o programa sem o for 
# para isso, criamos a seguinte variável para averiguar se é um palíndromo ou não
# inverso = frase[::-1]

for letra in range(len(frase) -1, -1,-1):
    inverso += frase[letra]

print(frase, inverso)
if frase == inverso:
    print("É um palíndromo.")
else:
    print("Não é palíndromo.")