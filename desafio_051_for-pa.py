#desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informa a razão da PA: "))
pa = []

print(f"Calculando a progressão aritmética. O primeiro termo é {termo} com razão {razao}.")
for c in range(1, 11):
    pa.append(termo)
    termo += razao
print(pa)