from math import trunc

num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}.')

print(f'Outra maneira de mostrar apenas a parte inteira é usar simplesmente o int para converter o número float {int(num)}.')