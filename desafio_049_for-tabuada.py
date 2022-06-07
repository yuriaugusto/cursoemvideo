#refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for

tabuada = int(input("Quer saber a tabuada de qual número? "))

print(f"Tabuada do {tabuada}")

for c in range(1, 11):
    print(f"{tabuada} x {c} = {tabuada*c}")