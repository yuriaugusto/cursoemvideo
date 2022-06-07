#desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor dele for impar, desconsidere-o

numlista = []
soma = 0

for c in range(0, 6):
    num = int(input(f"Digite o {c+1}º número: "))
    numlista.append(num)

for n in numlista:
    if n % 2 == 0:
        soma += n
print(numlista)
print(soma)